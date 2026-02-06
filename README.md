# MiSTercade Mapping Repositories

Pre-built arcade controller mappings for the [MiSTercade](https://misteraddons.com/products/mistercade) JAMMA interface board. These mappings are delivered to your MiSTer via the [MiSTer Downloader](https://github.com/MiSTer-devel/Downloader_MiSTer).

## Quick Start

1. Identify your MiSTercade version (printed on the board or shown in the OSD).
2. Choose a mapping variant from the table below.
3. Add the `downloader.ini` snippet to your MiSTer SD card.
4. Run **update_all** or **downloader**.

> **Only add ONE mapping repository per MiSTercade version.** Adding multiple variants for the same version will cause conflicts.

## Mapping Variants

Each MiSTercade version has four mapping variants:

| Variant | Menu Combo | Freeplay | Best for |
|---------|-----------|----------|----------|
| **Standard** | Down + Start opens OSD | No | General use |
| **Freeplay** | Down + Start opens OSD | Yes (start triggers coin) | Home / casual use |
| **No-Menu** | Disabled | No | Tournaments / competitive play |
| **No-Menu Freeplay** | Disabled | Yes (start triggers coin) | Tournament cabinets with freeplay |

## MiSTercade V1 (VID_PID `16D0_10BE`) &mdash; Deprecated

> **MiSTercade V1 mappings are deprecated.** A change to Jotego's JTFrame caused ghost inputs between player joysticks on all V1.X boards. A [firmware update](https://github.com/misteraddons/MiSTercadeV1/raw/6b9ab2dd289305a56be9a2f173248b50224aae19/firmware/_MiSTercade_V1-2025.zip) resolves this issue. If you use Jotego's cores, please update to **V1-2025** (see below). For full details, see the [MiSTerAddons blog post](https://misteraddons.com/blogs/news/mistercade-pre-order-firmware-update-and-pre-configured-input-mappings).

<details><summary><b>Standard</b> &mdash; menu combo enabled</summary>

```ini
[misteraddons/mistercade_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_mappings/db/db.json.zip
```
</details>

<details><summary><b>Freeplay</b> &mdash; menu combo enabled, start triggers coin</summary>

```ini
[misteraddons/mistercade_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_freeplay_mappings/db/db.json.zip
```
</details>

<details><summary><b>No-Menu</b> &mdash; menu combo disabled</summary>

```ini
[misteraddons/mistercade_nomenu_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_nomenu_mappings/db/db.json.zip
```
</details>

<details><summary><b>No-Menu Freeplay</b> &mdash; menu combo disabled, start triggers coin</summary>

```ini
[misteraddons/mistercade_nomenu_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_nomenu_freeplay_mappings/db/db.json.zip
```
</details>

## MiSTercade V1-2025 (VID_PID `16D0_10BE`)

V1-2025 is the updated firmware for all MiSTercade V1.X boards. It fixes ghost inputs caused by changes in Jotego's JTFrame and resolves a USB connection bug affecting some V1.0, V1.1, and V1.2 users.

<details><summary><b>Updating from V1 to V1-2025</b></summary>

1. [Download the V1-2025 firmware](https://github.com/misteraddons/MiSTercadeV1/raw/6b9ab2dd289305a56be9a2f173248b50224aae19/firmware/_MiSTercade_V1-2025.zip)
2. Extract the zip to the `Scripts` folder on your MiSTer micro SD card
3. (Optional) Add a V1-2025 mapping entry to `downloader.ini` (see snippets below)
4. Connect a USB keyboard or controller
5. Remove the MiSTercade top plate and place a pin jumper on the **STM32 DFU** 2-pin header
6. Boot MiSTer and navigate to `Scripts/MiSTercade_V1-2025` using your keyboard or controller
7. Select `mistercade_firmware_updater-local.sh`
8. After the script completes, power off, move the jumper back, and replace the top plate
9. Boot MiSTer and run **update_all** or **downloader** to acquire the new mappings

</details>

<details><summary><b>Standard</b> &mdash; menu combo enabled</summary>

```ini
[misteraddons/mistercade_v1_2025_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v1_2025_mappings/db/db.json.zip
```
</details>

<details><summary><b>Freeplay</b> &mdash; menu combo enabled, start triggers coin</summary>

```ini
[misteraddons/mistercade_v1_2025_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v1_2025_freeplay_mappings/db/db.json.zip
```
</details>

<details><summary><b>No-Menu</b> &mdash; menu combo disabled</summary>

```ini
[misteraddons/mistercade_v1_2025_nomenu_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v1_2025_nomenu_mappings/db/db.json.zip
```
</details>

<details><summary><b>No-Menu Freeplay</b> &mdash; menu combo disabled, start triggers coin</summary>

```ini
[misteraddons/mistercade_v1_2025_nomenu_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v1_2025_nomenu_freeplay_mappings/db/db.json.zip
```
</details>

## MiSTercade V2 (VID_PID `16D0_1358`)

<details><summary><b>Standard</b> &mdash; menu combo enabled</summary>

```ini
[misteraddons/mistercade_v2_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v2_mappings/db/db.json.zip
```
</details>

<details><summary><b>Freeplay</b> &mdash; menu combo enabled, start triggers coin</summary>

```ini
[misteraddons/mistercade_v2_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v2_freeplay_mappings/db/db.json.zip
```
</details>

<details><summary><b>No-Menu</b> &mdash; menu combo disabled</summary>

```ini
[misteraddons/mistercade_v2_nomenu_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v2_nomenu_mappings/db/db.json.zip
```
</details>

<details><summary><b>No-Menu Freeplay</b> &mdash; menu combo disabled, start triggers coin</summary>

```ini
[misteraddons/mistercade_v2_nomenu_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v2_nomenu_freeplay_mappings/db/db.json.zip
```
</details>

## How to Install

Edit the file `downloader.ini` at the root of your MiSTer SD card (create it if it doesn't exist). Add the snippet for your chosen variant to the end of the file. Then run **downloader** or **update_all**.

### Automated Setup

You can also run the setup script directly on your MiSTer via SSH:

```bash
curl -sSL https://raw.githubusercontent.com/misteraddons/mistercade_mappings/main/mistercade_mapping_setup.sh -o /tmp/mistercade_mapping_setup.sh && bash /tmp/mistercade_mapping_setup.sh
```

The script auto-detects your MiSTercade version via USB, lets you choose a mapping variant, backs up your existing `downloader.ini`, and applies the change.

For non-interactive use (e.g., scripting):

```bash
bash mistercade_mapping_setup.sh --version v2 --variant nomenu
```

## Switching Variants

To switch from one variant to another (e.g., from Standard to No-Menu), edit `downloader.ini` and remove the old `[misteraddons/mistercade_...]` section, then add the new one. Or re-run the setup script.

## Variant Details

### Menu Combo (Down + Start)
The standard and freeplay mappings include a two-button shortcut (Down + Start) that opens the MiSTer OSD menu. This is convenient for home use but can be accidentally triggered during gameplay. The **No-Menu** variants disable this shortcut entirely.

### Freeplay
Freeplay variants map the Coin button as an alternate input on Start, so pressing start also inserts a coin. This is useful for cabinets set to free play where you want a single button press to start the game. Console cores (NES, SNES, Genesis, etc.) are excluded from freeplay mapping.

## All Repositories

| MiSTercade | Standard | Freeplay | No-Menu | No-Menu Freeplay |
|----------|----------|----------|---------|------------------|
| V1 (deprecated) | [mappings](https://github.com/misteraddons/mistercade_mappings) | [freeplay](https://github.com/misteraddons/mistercade_freeplay_mappings) | [nomenu](https://github.com/misteraddons/mistercade_nomenu_mappings) | [nomenu freeplay](https://github.com/misteraddons/mistercade_nomenu_freeplay_mappings) |
| V1-2025 | [mappings](https://github.com/misteraddons/mistercade_v1_2025_mappings) | [freeplay](https://github.com/misteraddons/mistercade_v1_2025_freeplay_mappings) | [nomenu](https://github.com/misteraddons/mistercade_v1_2025_nomenu_mappings) | [nomenu freeplay](https://github.com/misteraddons/mistercade_v1_2025_nomenu_freeplay_mappings) |
| V2 | [mappings](https://github.com/misteraddons/mistercade_v2_mappings) | [freeplay](https://github.com/misteraddons/mistercade_v2_freeplay_mappings) | [nomenu](https://github.com/misteraddons/mistercade_v2_nomenu_mappings) | [nomenu freeplay](https://github.com/misteraddons/mistercade_v2_nomenu_freeplay_mappings) |
| V3 (pre-release) | [mappings](https://github.com/misteraddons/mistercade_v3_mappings) | [freeplay](https://github.com/misteraddons/mistercade_v3_freeplay_mappings) | [nomenu](https://github.com/misteraddons/mistercade_v3_nomenu_mappings) | [nomenu freeplay](https://github.com/misteraddons/mistercade_v3_nomenu_freeplay_mappings) |
