# MiSTercade V2 GamecontrollerDB

Download your preferred `downloader_[configuration name].ini` file and place it in `/media/fat` on your SD card.

You can only have one downloader ini per MiSTercade version. Multiple downloader ini files for the same version will overwrite each other.

## Options

- `freeplay` maps Player 1 Start as a credit/start shortcut where the core is eligible.
- `osd` selects the OSD/menu-combo database family.
- `nomenu` selects the no-menu-combo database family.

Important: `gamecontrollerdb_user.txt` does not include the MiSTercade `.map` pause/core credits feature.

## Files

| File | Freeplay | Menu Combo | Database ID |
| --- | --- | --- | --- |
| `downloader_gamecontrollerdb-v2-osd.ini` | No | OSD/menu combo | `misteraddons/MiSTercade/gamecontrollerdb-v2-osd` |
| `downloader_gamecontrollerdb-v2-freeplay-osd.ini` | Yes | OSD/menu combo | `misteraddons/MiSTercade/gamecontrollerdb-v2-freeplay-osd` |
| `downloader_gamecontrollerdb-v2-nomenu.ini` | No | No menu combo | `misteraddons/MiSTercade/gamecontrollerdb-v2-nomenu` |
| `downloader_gamecontrollerdb-v2-freeplay-nomenu.ini` | Yes | No menu combo | `misteraddons/MiSTercade/gamecontrollerdb-v2-freeplay-nomenu` |
