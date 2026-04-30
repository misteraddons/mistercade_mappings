# MiSTercade

This repo has MiSTercade mappings, firmware files, and installer scripts organized by MiSTercade version.

## Recommended Installer

1. Download [`mistercade_mapping_installer.sh`](mistercade_mapping_installer.sh) to your MiSTer SD card.
2. Run the installer on MiSTer.
3. Choose your MiSTercade version.
4. Choose `.map` files or the experimental `gamecontrollerdb_user.txt` option.
5. Choose whether you want freeplay.
6. Choose whether you want the MiSTer menu/OSD button combo when installing `.map` files.
7. Optionally configure `MiSTer.ini` for MiSTercade video and controller settings.
8. Run your MiSTer updater script.

The installer shows the MiSTercade mappings already configured on your SD card before you change anything.

The installer checks for MiSTercade sections in `/media/fat/downloader.ini` and can back up that file before removing those sections.

The installer checks for existing MiSTercade `downloader_*.ini` files in `/media/fat` and removes conflicting choices for the MiSTercade version you select.

The installer checks for existing `/media/fat/config/inputs/*_VID_PID_v3.map` files matching your selected MiSTercade version and can create a timestamped backup archive before you continue.

The installer checks for `/media/fat/gamecontrollerdb/gamecontrollerdb_user.txt` and can back it up and remove it when you switch back to `.map` files.

The installer can back up and update `/media/fat/MiSTer.ini` with MiSTercade-friendly settings. The shared V1/V2 video settings are `direct_video=2`, `composite_sync=1`, and `vga_mode=rgb`.

The installer downloads the selected `downloader_[configuration name].ini` file to `/media/fat`.

## Manual Install

1. Open the folder for your MiSTercade version.
2. Open the `mappings/` folder.
3. Download your preferred `downloader_[configuration name].ini` file and place it in `/media/fat` on your SD card.
4. Run your MiSTer updater script.

Firmware files and flashing scripts are in each version's `firmware/` folder when firmware is available.

When you run your MiSTer updater script, it will download all MiSTercade mappings. As new arcade cores are released, more mappings will be added. Your MiSTer updater will automatically download them.

### Note

You can only have one downloader ini per MiSTercade version. Multiple downloader ini files for the same version will overwrite each other.

### Compatibility Notes

- Twin-stick/right-stick mappings are generated when the source MRA exposes those controls. Legacy V2 notes list twin-stick mappings as a known gap, so treat V2 twin-stick support as limited.

### Folders

- Each MiSTercade version folder contains `mappings/` for MiSTer `.map` downloader choices.
- Version folders may also contain `firmware/` with firmware binaries, flashing instructions, checksums, and notes.
- `gamecontrollerdb/` installs `gamecontrollerdb/gamecontrollerdb_user.txt` instead of `.map` files. This option is experimental and hasn't been tested.
- MiSTercade V1 non-2025 is legacy/deprecated due to Jotego framework changes. Use MiSTercade V1 2025 whenever possible.

| Folder | Hardware | Contains |
| --- | --- | --- |
| [`mistercade_v1/`](mistercade_v1/) | MiSTercade V1 | mappings |
| [`mistercade_v1_2025/`](mistercade_v1_2025/) | MiSTercade V1 2025 | mappings, gamecontrollerdb, firmware |
| [`mistercade_v2/`](mistercade_v2/) | MiSTercade V2 | mappings, gamecontrollerdb, firmware |
