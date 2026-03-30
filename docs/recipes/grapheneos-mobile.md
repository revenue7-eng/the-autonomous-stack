---
title: "GrapheneOS Mobile Stack"
parent: Recipes
nav_order: 9
---

# GrapheneOS Mobile Stack

Build a fully autonomous phone — no Google account, no tracking, no cloud dependency. This recipe starts with the operating system and works up through apps for every daily task.

All components are **A3/T2** (fully autonomous, open source) unless noted.

---

## Goal

A phone that:

- Runs without a Google account
- Does not send telemetry or location data
- Handles messaging, email, photos, navigation, passwords, and 2FA
- Syncs with your self-hosted server (optional)
- Can be wiped and rebuilt in under an hour

You will end up with a daily-driver phone that respects Pause, Exit, and Recoverability.

---

## Requirements

- **Google Pixel** device (Pixel 6 or newer recommended)
- A computer with a web browser and USB cable
- 30–60 minutes for initial setup
- Optional: a self-hosted server ([Minimal Autonomous Server](minimal-server.md)) for photo sync and file storage

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **GrapheneOS** | [`compute/os`](../catalog/grapheneos.md) | Mobile operating system |
| **F-Droid** | [`mobile/app-store`](../catalog/f-droid.md) | App store |
| **Aurora Store** | [`mobile/app-store`](../catalog/aurora-store.md) | Play Store bridge (no account) |
| **Signal** | [`communication/messaging`](../catalog/signal.md) | Encrypted messaging |
| **SimpleX Chat** | [`communication/messaging`](../catalog/simplex-chat.md) | Anonymous messaging |
| **K-9 Mail** | [`communication/email`](../catalog/k9-mail.md) | Email client |
| **Ente Photos** | [`applications/photos`](../catalog/ente-photos.md) | Encrypted photo backup |
| **Aegis** | [`security/2fa`](../catalog/aegis.md) | 2FA authenticator |
| **Bitwarden / Vaultwarden** | [`security/passwords`](../catalog/vaultwarden.md) | Password manager |
| **OsmAnd** | [`mobile/navigation`](../catalog/osmand.md) | Offline maps |
| **Mull** | [`mobile/browser`](../catalog/mull.md) | Hardened browser |
| **HeliBoard** | [`mobile/keyboard`](../catalog/heliboard.md) | Private keyboard |
| **NewPipe** | [`applications/media`](../catalog/newpipe.md) | YouTube without Google |
| **Syncthing** | [`storage/sync`](../catalog/syncthing.md) | File sync (optional) |

*All are A3/T2.*

---

## Step-by-Step Instructions

### 1. Install GrapheneOS

GrapheneOS has a web installer — no command line needed.

1. On your computer, open [https://grapheneos.org/install/web](https://grapheneos.org/install/web)
2. Enable OEM unlocking on your Pixel: Settings → About phone → tap Build number 7 times → Developer options → OEM unlocking
3. Connect Pixel to computer via USB
4. Follow the web installer — it will unlock bootloader, flash GrapheneOS, and relock bootloader
5. Reboot into GrapheneOS

**Important:** Relocking the bootloader enables verified boot — do not skip this step.

After first boot:
- Skip Wi-Fi during initial setup (you can add it after)
- Do not add any Google account
- Set a strong PIN or passphrase

### 2. Install App Stores

GrapheneOS has no app store by default. Install F-Droid first, then use it for everything else.

**F-Droid:**
1. Open the built-in Vanadium browser
2. Go to [https://f-droid.org](https://f-droid.org)
3. Download the APK and install
4. Open F-Droid → Settings → Repositories → ensure "F-Droid" and "F-Droid Archive" are enabled

**Neo Store** (optional, better UI):
1. In F-Droid, search for "Neo Store"
2. Install and use as your primary F-Droid client

**Aurora Store** (for apps not on F-Droid):
1. In F-Droid, search for "Aurora Store"
2. Install, open, choose "Anonymous" login
3. Use only when F-Droid does not have what you need

### 3. Replace the Keyboard

Your keyboard sees everything you type. Replace it first.

1. Install **HeliBoard** from F-Droid
2. Go to Settings → System → Languages & input → On-screen keyboard
3. Enable HeliBoard, disable Vanadium keyboard
4. Open HeliBoard → download dictionaries for your languages

HeliBoard has no internet permission — keystrokes never leave your device.

### 4. Install Browser

1. Install **Mull** from F-Droid (DivestOS repo)
2. Open Mull → set as default browser
3. Change default search engine to DuckDuckGo or your SearXNG instance
4. Install uBlock Origin from Firefox Add-ons

Or keep Vanadium (GrapheneOS built-in, Chromium-based) as a secondary browser for compatibility.

### 5. Set Up Messaging

**Signal** (for contacts who use it):
1. Install from Aurora Store (not on F-Droid) or download APK from [signal.org/android](https://signal.org/android)
2. Register with your phone number
3. Enable disappearing messages by default: Settings → Privacy → Default timer

**SimpleX Chat** (for maximum privacy):
1. Install from F-Droid
2. No registration needed — create a profile name and start
3. Share connection links with contacts instead of phone numbers

### 6. Set Up Email

1. Install **K-9 Mail** from F-Droid
2. Add your email account (IMAP/SMTP)
3. Disable remote image loading: Settings → account → Fetching mail → disable "Show images"

If using a privacy email provider ([Tuta](../catalog/tuta.md), [Proton Mail](../catalog/protonmail.md)), install their dedicated app from Aurora Store.

### 7. Set Up Photo Backup

**Option A: Ente Photos** (easiest, works without self-hosting):
1. Install from F-Droid or Aurora Store
2. Create account — photos are E2E encrypted, Ente cannot see them
3. Enable auto-backup from camera folder

**Option B: Immich** (requires self-hosted server):
1. Install Immich app from Aurora Store
2. Point to your Immich server URL
3. Enable auto-backup

### 8. Set Up Passwords and 2FA

**Bitwarden** (connects to your Vaultwarden server or Bitwarden cloud):
1. Install from Aurora Store
2. Point to your Vaultwarden server URL, or use Bitwarden cloud
3. Enable biometric unlock
4. Enable auto-fill: Settings → Passwords & accounts → Bitwarden

**Aegis** (2FA):
1. Install from F-Droid
2. Set a vault password and enable biometric unlock
3. Import existing 2FA codes or scan new QR codes
4. Enable automatic encrypted backups to a local folder
5. Sync that folder to your server via Syncthing (optional)

### 9. Set Up Navigation

1. Install **OsmAnd** from F-Droid (free, all features)
2. Download maps for your country/region
3. Test offline navigation — disconnect Wi-Fi and navigate somewhere

Your location data never leaves the device.

### 10. Set Up Media

**NewPipe** (YouTube without Google):
1. Install from F-Droid
2. Import your YouTube subscriptions (export from Google Takeout as OPML, import into NewPipe)
3. Download videos for offline viewing

**AntennaPod** (podcasts):
1. Install from F-Droid
2. Search for podcasts or import OPML from your previous app
3. Set auto-download for offline listening

### 11. Optional: Connect to Self-Hosted Server

If you have a [Minimal Autonomous Server](minimal-server.md) or similar:

**Syncthing** — sync files, Aegis backups, documents:
1. Install from F-Droid
2. Add your server as a device (scan QR code)
3. Share folders: camera backups, documents, 2FA backups

**Nextcloud** — calendar, contacts, files:
1. Install from F-Droid
2. Connect to your Nextcloud instance
3. Enable contact and calendar sync via DAVx⁵ (install from F-Droid)

**WireGuard** — secure access to home network:
1. Install from F-Droid
2. Import your VPN config (scan QR from your server)
3. Enable always-on VPN: Settings → Network → VPN → WireGuard → Always-on

### 12. Sandboxed Google Play (If Needed)

Some apps (banking, transport) require Google Play Services. GrapheneOS lets you install them sandboxed — no special privileges.

1. Settings → Apps → Install Google Play Services (built into GrapheneOS)
2. Google Play runs in a sandboxed profile — it cannot access other apps' data
3. Create a separate user profile for apps that need Google: Settings → System → Multiple users

This keeps Google confined. Your primary profile stays clean.

---

## Failure Modes

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **GrapheneOS** | Failed OTA update | Phone may not boot | Boot to recovery, factory reset, restore from backup |
| **F-Droid** | Repository down | Cannot install new apps | Apps already installed work. Use Aurora Store or direct APK. |
| **Signal** | Phone number change | Lose access to account | Re-register with new number. Message history from backup. |
| **Aegis** | Phone lost/stolen | Lose 2FA codes | Restore from encrypted backup (stored on Syncthing/server) |
| **OsmAnd** | Outdated maps | Incorrect routing | Re-download maps when online |
| **Aurora Store** | Anonymous login blocked | Cannot download Play Store apps | Wait for new session, or use APKPure/direct APK download |
| **Sandboxed Play** | Google Services crash | Banking/transport apps fail | Restart Play Services, or use browser versions of services |

**Highest-impact failure:** losing Aegis 2FA codes without backup. Set up Syncthing backup of Aegis vault on day one.

---

## Verification

After setup, verify the three structural criteria:

- **Pause:** Turn on airplane mode. Messaging (cached), maps (offline), photos (local), passwords (local vault), 2FA (offline) — all work. Only Signal/email need internet to send/receive.
- **Exit:** All data is on-device or in standard formats. Export contacts (VCF), photos (JPEG/PNG), passwords (Bitwarden export), 2FA (Aegis JSON), subscriptions (OPML). Flash stock Android and you're back to factory.
- **Recoverability:** Factory reset GrapheneOS, reinstall apps from F-Droid, restore Aegis vault from Syncthing backup, restore Bitwarden from server. Under one hour.

---

## What It Replaces

| Need | Was | Now | Monthly savings |
|------|-----|-----|-----------------|
| Phone OS | Stock Android + Google | GrapheneOS | $0 (free) |
| App store | Google Play | F-Droid + Aurora | $0 |
| Messaging | WhatsApp / Telegram | Signal + SimpleX | $0 |
| Photos | Google Photos (15 GB free, then $3/mo) | Ente Photos / Immich | $0–3 |
| Maps | Google Maps | OsmAnd | $0 |
| Passwords | LastPass ($3/mo) | Bitwarden / Vaultwarden | $3 |
| 2FA | Google Authenticator | Aegis | $0 |
| YouTube | YouTube (ads or $14/mo) | NewPipe | $14 |

**Total potential savings: ~$20/month, plus you own your data.**

---

## Next Steps

- Set up a [Minimal Autonomous Server](minimal-server.md) to self-host the backend
- Browse the full [Mobile Apps](../mobile.html) page for more alternatives
- Add [Nextcloud](../catalog/nextcloud.md) for calendar, contacts, and office documents
- Explore the [Family Cloud](family-cloud.md) recipe for shared photo and file storage
