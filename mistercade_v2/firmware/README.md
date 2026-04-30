# MiSTercade V2 Firmware

These files are staged when the consolidated main branch is generated.

Only flash firmware that matches your MiSTercade hardware.

MiSTercade V2 uses GP2040-CE UF2 firmware.

This folder intentionally publishes only the current official MiSTercade V2 UF2 from the latest GP2040-CE release.

## Flashing

These steps follow the MiSTercade V2 firmware repo instructions, adjusted for the single UF2 file published here.

1. Download the UF2 file to your computer, or copy it to the MiSTer SD card under `/media/fat/Scripts/_MiSTercade_V2_/`.
2. Hold `JOY1 PROG`, `JOY2 PROG`, or both buttons on the MiSTercade PCB while powering on MiSTercade. Each held player controller enters RP2040 bootloader mode.
3. If flashing from a computer, connect the MiSTercade micro USB port. The bootloader drive appears as `RPI-RP2`; copy the UF2 file to that drive.
4. If flashing from MiSTer, open a terminal with `F9` or SSH, then copy the UF2 to the mounted bootloader drive.

Player 1:

```sh
cp /media/fat/Scripts/_MiSTercade_V2_/GP2040-CE_0.7.12_MiSTercadeV2.uf2 /media/usb0
```

Player 2:

```sh
cp /media/fat/Scripts/_MiSTercade_V2_/GP2040-CE_0.7.12_MiSTercadeV2.uf2 /media/usb1
```

5. Wait for the bootloader drive to disconnect/reboot, then power cycle MiSTercade.
6. If you only held one `PROG` button, repeat the process for the other player controller.

The sibling V2 firmware repo previously included helper scripts that copied the firmware to `/media/usb0` and `/media/usb1`. This folder intentionally publishes only the current firmware UF2, so the commands above are the direct equivalent.

## Files

| File | Size | SHA256 | Notes |
| --- | ---: | --- | --- |
| `GP2040-CE_0.7.12_MiSTercadeV2.uf2` | 2427392 | `129c6dca7a0cac38fd3788bae0a311b103c23b0ad9443cf2a0b912e74d77b83c` | Latest official GP2040-CE MiSTercade V2 firmware (v0.7.12). |

Machine-readable checksums are also available in [`manifest.json`](manifest.json).
