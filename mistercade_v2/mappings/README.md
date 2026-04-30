# MiSTercade V2 Map Files

Download your preferred `downloader_[configuration name].ini` file and place it in `/media/fat` on your SD card.

You can only have one downloader ini per MiSTercade version. Multiple downloader ini files for the same version will overwrite each other.

Twin-stick/right-stick mappings are generated when the source MRA exposes those controls. Legacy V2 notes list twin-stick mappings as a known gap, so treat V2 twin-stick support as limited.

## Options

- `freeplay` maps Player 1 Start as a credit/start shortcut where the core is eligible.
- `osd` includes the MiSTer menu/OSD combo in the main/default input map. Game-specific `.map` files are the same as the matching `nomenu` variant.
- `nomenu` leaves the MiSTer menu/OSD combo out of the main/default input map.

## Files

| File | Freeplay | Menu Combo | Database ID |
| --- | --- | --- | --- |
| `downloader_maps-v2-osd.ini` | No | OSD/menu combo | `misteraddons/MiSTercade/maps-v2-osd` |
| `downloader_maps-v2-freeplay-osd.ini` | Yes | OSD/menu combo | `misteraddons/MiSTercade/maps-v2-freeplay-osd` |
| `downloader_maps-v2-nomenu.ini` | No | No menu combo | `misteraddons/MiSTercade/maps-v2-nomenu` |
| `downloader_maps-v2-freeplay-nomenu.ini` | Yes | No menu combo | `misteraddons/MiSTercade/maps-v2-freeplay-nomenu` |
