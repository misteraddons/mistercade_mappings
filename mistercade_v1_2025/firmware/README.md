# MiSTercade V1 2025 Firmware

These files are staged when the consolidated main branch is generated.

Only flash firmware that matches your MiSTercade hardware.

This is the recommended firmware update for MiSTercade V1 hardware.

## Flashing

These steps follow the MiSTercade V1 firmware repo instructions, adjusted for the files in this folder.

1. Download and extract `_MiSTercade_V1-2025.zip` to the MiSTer SD card, or copy `MiSTercade_FW.bin`, `hid-flash_MiSTer`, and `mistercade_firmware_updater-local.sh` into the same folder.
2. Power off MiSTer/MiSTercade and place the jumper on the `STM32 DFU` header pins.
3. Plug in a USB keyboard, power on MiSTer, then open a terminal with `F9` or connect by SSH as `root` with password `1`.
4. Run `lsusb` and confirm `1209:babe` appears. That is the STM32 HID bootloader.
5. Change into the folder containing the firmware files.
6. Run `chmod +x hid-flash_MiSTer mistercade_firmware_updater-local.sh`.
7. Run `./mistercade_firmware_updater-local.sh`.
8. When the updater completes, power off, remove the `STM32 DFU` jumper, and restart MiSTercade.
9. Optional verification: run `lsusb` again and confirm `8888:8888` appears for the controller firmware.

Manual flash command:

```sh
./hid-flash_MiSTer MiSTercade_FW.bin
```

## Files

| File | Size | SHA256 | Notes |
| --- | ---: | --- | --- |
| `MiSTercade_FW.bin` | 4816 | `9802027ff0b8941c9b6dbcbc223f887aaf966259582692eedf3c7383a56b26d5` | V1 2025 firmware binary. |
| `_MiSTercade_V1-2025.zip` | 20065 | `f1f4753f822eae5c4af632fe05d858fa4f275319f54a2e2e8e7f9f0013fdd1d3` | Original V1 2025 firmware package. |
| `hid-flash_MiSTer` | 29884 | `064ff721e79eba287b6a010b743d0df7b0f03f44748a096e6a1a9b801c33ebe0` | MiSTer-side HID flasher for V1 firmware. |
| `mistercade_firmware_updater-local.sh` | 1547 | `977d00e5398880ed03e202ace765830211c967a7d45213df7c25f3f3355d3819` | Local V1 firmware updater script. |

Machine-readable checksums are also available in [`manifest.json`](manifest.json).
