---
title: "Monitoring Stack"
parent: Recipes
nav_order: 5
---

# Monitoring Stack

You deployed your infrastructure. Now you need to see what's happening inside it. This recipe builds a complete monitoring and alerting stack — metrics, logs, uptime checks, and security — all self-hosted.

This is a **companion recipe**: it plugs into any of the other TAS recipes (Minimal Server, Family Cloud, Privacy Homelab, Developer Workstation) and gives you visibility into everything that's running.

---

## Goal

Build a monitoring stack that:

- Collects metrics from all your containers and the host (CPU, RAM, disk, network)
- Stores and visualizes metrics with dashboards
- Aggregates logs from all services in one place
- Monitors uptime and alerts you when something goes down
- Detects and blocks malicious traffic (brute force, port scans)
- Runs entirely self-hosted — no cloud telemetry services

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Debian** | [`compute/os`](../catalog/debian.md) | Base operating system (or any Linux with Docker) |
| **Prometheus** | [`observability/metrics`](../catalog/prometheus.md) | Metrics collection and storage |
| **Grafana** | [`observability/dashboards`](../catalog/grafana.md) | Dashboards and visualization |
| **Loki** | [`observability/metrics`](../catalog/loki.md) | Log aggregation |
| **Uptime Kuma** | [`observability/monitoring`](../catalog/uptime-kuma.md) | Uptime monitoring and alerting |
| **CrowdSec** | [`security`](../catalog/crowdsec.md) | Intrusion detection and prevention |
| **Netdata** | [`observability/monitoring`](../catalog/netdata.md) | Real-time host metrics (lightweight agent) |

*All are A3/T2, except CrowdSec (A2/T2 — crowdsourced blocklist requires internet).*

---

## Who is this for?

- Anyone running TAS recipes who wants to know what's happening
- Homelabbers who are tired of SSHing in to check if services are running
- Anyone who has lost data because they didn't notice a disk filling up
- People who want to detect attacks before they succeed

**Estimated setup time:** 1–2 hours.
**Additional resources:** ~1 GB RAM for the monitoring stack itself. Prometheus retention grows ~50 MB/day for a typical homelab.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Your Services                     │
│  (Nextcloud, Immich, Forgejo, Jellyfin, etc.)       │
└─────────┬──────────────────┬───────────────────┬────┘
          │ metrics          │ logs              │ HTTP
          ▼                  ▼                   ▼
   ┌──────────┐      ┌──────────┐        ┌───────────┐
   │Prometheus│      │   Loki   │        │Uptime Kuma│
   │ (scrape) │      │(receive) │        │  (probe)  │
   └────┬─────┘      └────┬─────┘        └─────┬─────┘
        │                  │                    │
        └──────────┬───────┘                    │
                   ▼                            │
             ┌──────────┐                       │
             │ Grafana  │◄──────────────────────┘
             │(dashboards)│
             └──────────┘

   ┌──────────┐      ┌──────────┐
   │ Netdata  │      │ CrowdSec │
   │(host CPU,│      │  (IDS/   │
   │ RAM, I/O)│      │   IPS)   │
   └──────────┘      └──────────┘
```

---

## Step-by-Step Instructions

### 1. Create Project Directory

```bash
mkdir -p /opt/monitoring && cd /opt/monitoring
```

### 2. Create Docker Compose

```bash
cat > docker-compose.yml << 'YAMLEOF'
services:

  # ── Metrics ────────────────────────────────────────
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./config/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./data/prometheus:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=90d'
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:9090/-/healthy"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Dashboards ─────────────────────────────────────
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: CHANGE_ME_GRAFANA_PASSWORD
    volumes:
      - ./data/grafana:/var/lib/grafana
      - ./config/grafana/provisioning:/etc/grafana/provisioning
    depends_on:
      prometheus:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:3000/api/health"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Logs ───────────────────────────────────────────
  loki:
    image: grafana/loki:latest
    container_name: loki
    ports:
      - "3100:3100"
    volumes:
      - ./config/loki/loki-config.yml:/etc/loki/local-config.yaml
      - ./data/loki:/loki
    command: -config.file=/etc/loki/local-config.yaml
    restart: unless-stopped

  # ── Uptime Monitoring ──────────────────────────────
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    ports:
      - "3001:3001"
    volumes:
      - ./data/uptime-kuma:/app/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:3001"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Host Metrics ───────────────────────────────────
  netdata:
    image: netdata/netdata:latest
    container_name: netdata
    ports:
      - "19999:19999"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
    cap_add:
      - SYS_PTRACE
    security_opt:
      - apparmor:unconfined
    restart: unless-stopped

  # ── Security (IDS/IPS) ────────────────────────────
  crowdsec:
    image: crowdsecurity/crowdsec:latest
    container_name: crowdsec
    ports:
      - "8080:8080"
    volumes:
      - ./config/crowdsec:/etc/crowdsec
      - ./data/crowdsec:/var/lib/crowdsec/data
      - /var/log:/var/log:ro
    environment:
      COLLECTIONS: "crowdsecurity/linux crowdsecurity/docker"
    restart: unless-stopped
YAMLEOF
```

### 3. Configure Prometheus

```bash
mkdir -p config/prometheus
cat > config/prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'netdata'
    metrics_path: '/api/v1/allmetrics?format=prometheus'
    static_configs:
      - targets: ['netdata:19999']

  - job_name: 'docker-containers'
    static_configs:
      - targets: ['host.docker.internal:9323']
EOF
```

**To monitor other services:** add targets for any service that exposes a `/metrics` endpoint. Many TAS catalog services do: PostgreSQL (via postgres_exporter), Traefik, Forgejo, etc.

### 4. Configure Loki

```bash
mkdir -p config/loki
cat > config/loki/loki-config.yml << 'EOF'
auth_enabled: false

server:
  http_listen_port: 3100

common:
  path_prefix: /loki
  storage:
    filesystem:
      chunks_directory: /loki/chunks
      rules_directory: /loki/rules
  replication_factor: 1
  ring:
    kvstore:
      store: inmemory

schema_config:
  configs:
    - from: 2020-10-24
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

limits_config:
  retention_period: 30d
EOF
```

### 5. Configure Grafana Datasources

```bash
mkdir -p config/grafana/provisioning/datasources
cat > config/grafana/provisioning/datasources/datasources.yml << 'EOF'
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true

  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
EOF
```

### 6. Deploy

```bash
cd /opt/monitoring
docker compose up -d
```

### 7. Access Dashboards

| Service | URL | Purpose |
|---------|-----|---------|
| Grafana | `http://your-server:3000` | Metrics dashboards, log viewer |
| Prometheus | `http://your-server:9090` | Raw metrics, query explorer |
| Uptime Kuma | `http://your-server:3001` | Uptime status page |
| Netdata | `http://your-server:19999` | Real-time host metrics |

**First steps in Grafana:**
1. Log in with admin / your password
2. Go to Dashboards → Import
3. Import dashboard ID `1860` (Node Exporter Full) for host metrics
4. Import dashboard ID `14282` (Docker) for container metrics
5. Explore → select Loki → view logs from all services

### 8. Set Up Alerts in Uptime Kuma

Add monitors for each of your services:

1. Open Uptime Kuma at `:3001`
2. Add HTTP monitors for each service URL
3. Set up a notification method: Telegram, email, Discord, or Gotify
4. Recommended monitors:
   - All web UIs (Nextcloud, Immich, Grafana, etc.)
   - PostgreSQL (TCP port 5432)
   - DNS (query test against AdGuard/Pi-hole)

---

## Failure Modes

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **Prometheus** | Disk full | Metrics stop being collected | Reduce retention: `--storage.tsdb.retention.time=30d`. Prune old data. |
| **Grafana** | Database corruption | Dashboards lost | Re-import dashboards (they're just JSON). Data is in Prometheus/Loki. |
| **Loki** | Ingestion overload | Logs dropped | Check limits in loki-config.yml. Increase resources or reduce log verbosity. |
| **Uptime Kuma** | Service down | No alerts | Non-critical for operations. All services continue running. Restart container. |
| **Netdata** | High CPU usage | Host slowdown | Netdata can be resource-hungry. Reduce collection frequency or disable unused plugins. |
| **CrowdSec** | False positive blocks | Legitimate traffic blocked | Check decisions: `docker exec crowdsec cscli decisions list`. Remove bad decision: `cscli decisions delete --id <id>` |

**Key insight:** The monitoring stack itself is non-critical. If it goes down, your actual services (Nextcloud, Immich, etc.) are unaffected. Monitoring failure is invisible until you look — which is why Uptime Kuma monitoring itself (via an external probe) is valuable.

---

## Connecting to Other Recipes

This monitoring stack is designed to plug into any TAS recipe:

**Minimal Server:** Add Prometheus scrape targets for AdGuard, Authentik, Forgejo. Add Uptime Kuma monitors for all services.

**Family Cloud:** Monitor PostgreSQL (critical for Immich + Nextcloud), disk usage (photos fill up fast), Kopia backup status.

**Developer Workstation:** Monitor CI/CD pipelines (Woodpecker/Gitea Actions), Git push/pull latency, container resource usage.

To connect, add your service targets to `config/prometheus/prometheus.yml` and restart Prometheus:

```bash
docker compose restart prometheus
```

---

## Cost

| Item | Additional resource |
|------|-------------------|
| RAM | +1 GB |
| Disk (90 days metrics) | +5 GB |
| CPU | Minimal (Prometheus is efficient) |

No additional hardware needed — runs alongside your existing stack.
