---
title: "Docker"
category: "compute/container"
status: "stable"
license: "Apache-2.0"
source: "https://www.docker.com"
repository: "https://github.com/docker/docker-ce"
documentation: "https://docs.docker.com/engine/"
docker_image: "https://hub.docker.com/_/docker"
community: "https://forums.docker.com"
autonomy_level: "A3"
transparency_level: "T2"
---

# Docker

## Brief Description

Platform for developing, shipping, and running applications in lightweight containers. Works fully offline after images are downloaded.

## Architectural Role

Compute layer: provides container runtime and orchestration for services. The foundation for running autonomous stacks.

## Technical Autonomy

- ✅ Works without internet (after images are cached)
- ✅ Stores data locally (images, volumes, configuration)
- ✅ Does not require external accounts
- ✅ Allows data export (images, volumes, configs can be saved)
- ✅ Provides offline updates (manual via packages)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| Pause | Yes | Containers can be stopped, started, or paused at any time. |
| Exit | Yes | No lock-in; containers can be moved, exported, or replaced. |
| Recoverability | Yes | Volumes can be backed up; containers can be recreated from images. |
| Visibility | Yes | Open source, fully transparent. |
| External Dependencies | Yes | No cloud dependencies after setup; can run entirely offline. |

## Configuration (Minimal)

Installation (on Debian/Ubuntu):

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
```

Verify offline functionality:

```bash
# After downloading images, disconnect network and test:
docker run hello-world
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) – uses Docker to run all services.

## Alternatives

- Podman – daemonless, rootless, compatible with Docker CLI  
- containerd – lower-level runtime, used by Kubernetes  
- LXC/LXD – system containers, not application containers  

## Sources

- Website
https://www.docker.com

- Documentation
https://docs.docker.com/engine/

- Repository
https://github.com/docker/docker-ce

- Docker image
https://hub.docker.com/_/docker

- Community
https://forums.docker.com
