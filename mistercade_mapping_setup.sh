#!/bin/bash
#
# MiSTercade Mapping Setup Script
#
# Configures downloader.ini on a MiSTer to use the correct
# MiSTercade mapping repository for your firmware and preferences.
#
# Usage (run on MiSTer via SSH):
#   curl -sSL https://raw.githubusercontent.com/misteraddons/mistercade_mappings/main/mistercade_mapping_setup.sh -o /tmp/mistercade_mapping_setup.sh && bash /tmp/mistercade_mapping_setup.sh
#
# Non-interactive usage:
#   bash mistercade_mapping_setup.sh --version v2 --variant nomenu
#

set -e

DOWNLOADER_INI="/media/fat/downloader.ini"

# --- Argument parsing for non-interactive mode ---
ARG_VERSION=""
ARG_VARIANT=""

while [ $# -gt 0 ]; do
    case "$1" in
        --version)
            ARG_VERSION="$2"
            shift 2
            ;;
        --variant)
            ARG_VARIANT="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: mistercade_mapping_setup.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --version VERSION   MiSTercade version: v1, v1-2025, v2, v3"
            echo "  --variant VARIANT   Mapping variant: standard, freeplay, nomenu, nomenu-freeplay"
            echo "  --help              Show this help"
            echo ""
            echo "If no options are given, the script runs interactively."
            exit 0
            ;;
        *)
            echo "Unknown option: $1 (use --help for usage)"
            exit 1
            ;;
    esac
done

# --- Non-interactive mode ---
if [ -n "$ARG_VERSION" ] && [ -n "$ARG_VARIANT" ]; then
    case "$ARG_VERSION" in
        v1)       fw_prefix="" ;;
        v1-2025)  fw_prefix="v1_2025_" ;;
        v2)       fw_prefix="v2_" ;;
        v3)       fw_prefix="v3_" ;;
        *)
            echo "Invalid version: $ARG_VERSION (must be v1, v1-2025, v2, or v3)"
            exit 1
            ;;
    esac
    case "$ARG_VARIANT" in
        standard)         variant_suffix="mappings" ;;
        freeplay)         variant_suffix="freeplay_mappings" ;;
        nomenu)           variant_suffix="nomenu_mappings" ;;
        nomenu-freeplay)  variant_suffix="nomenu_freeplay_mappings" ;;
        *)
            echo "Invalid variant: $ARG_VARIANT (must be standard, freeplay, nomenu, or nomenu-freeplay)"
            exit 1
            ;;
    esac

    if [ -z "$fw_prefix" ]; then
        REPO_NAME="mistercade_${variant_suffix}"
    else
        REPO_NAME="mistercade_${fw_prefix}${variant_suffix}"
    fi
    DB_URL="https://raw.githubusercontent.com/misteraddons/${REPO_NAME}/db/db.json.zip"

    echo "Non-interactive mode: ${REPO_NAME}"
    # Skip to apply section
else

# --- Interactive mode ---
echo ""
echo "=========================================="
echo "  MiSTercade Mapping Setup"
echo "=========================================="
echo ""

# Show current configuration
if [ -f "$DOWNLOADER_INI" ]; then
    CURRENT=$(grep -oP '^\[misteraddons/\Kmistercade[^\]]*mappings' "$DOWNLOADER_INI" 2>/dev/null || true)
    if [ -n "$CURRENT" ]; then
        echo "Current mapping: ${CURRENT}"
        echo ""
    else
        echo "No MiSTercade mapping currently configured."
        echo ""
    fi
else
    echo "No downloader.ini found. One will be created."
    echo ""
fi

# --- Step 1: Detect MiSTercade version via USB VID:PID ---
fw_prefix=""
detected=""

if command -v lsusb > /dev/null 2>&1; then
    if lsusb -d 16d0:144f > /dev/null 2>&1; then
        detected="V3"
        fw_prefix="v3_"
        echo "Detected MiSTercade V3 (16D0:144F)"
    elif lsusb -d 16d0:1358 > /dev/null 2>&1; then
        detected="V2"
        fw_prefix="v2_"
        echo "Detected MiSTercade V2 (16D0:1358)"
    elif lsusb -d 16d0:10be > /dev/null 2>&1; then
        detected="V1/V1-2025"
        echo "Detected MiSTercade V1 or V1-2025 (16D0:10BE)"
        echo ""
        echo "V1 and V1-2025 share the same USB ID."
        echo "Which version do you have?"
        echo ""
        echo "  1) MiSTercade V1        (deprecated)"
        echo "  2) MiSTercade V1-2025   (2025 update)"
        echo ""
        read -p "Enter choice [1-2]: " v1_choice < /dev/tty
        case "$v1_choice" in
            1)
                fw_prefix=""
                echo ""
                echo "WARNING: MiSTercade V1 mappings are deprecated."
                echo "A change to Jotego's JTFrame caused ghost inputs on V1.X boards."
                echo "Please consider updating to V1-2025 firmware."
                echo "See: https://misteraddons.com/blogs/news/mistercade-pre-order-firmware-update-and-pre-configured-input-mappings"
                echo ""
                read -p "Continue with V1 anyway? [y/N]: " v1_confirm < /dev/tty
                if [ "$v1_confirm" != "y" ] && [ "$v1_confirm" != "Y" ]; then
                    echo "Exiting. Please update your firmware and re-run this script."
                    exit 0
                fi
                ;;
            2) fw_prefix="v1_2025_" ;;
            *)
                echo "Invalid choice. Exiting."
                exit 1
                ;;
        esac
    else
        echo "No MiSTercade detected on USB."
        echo ""
    fi
else
    echo "lsusb not found, skipping auto-detection."
    echo ""
fi

# If detection didn't identify a version, fall back to manual selection
if [ -z "$detected" ]; then
    echo "Which MiSTercade version do you have?"
    echo ""
    echo "  1) MiSTercade V1        (deprecated)"
    echo "  2) MiSTercade V1-2025   (2025 update)"
    echo "  3) MiSTercade V2"
    echo "  4) MiSTercade V3        (pre-release)"
    echo ""
    read -p "Enter choice [1-4]: " fw_choice < /dev/tty
    case "$fw_choice" in
        1)
            fw_prefix=""
            echo ""
            echo "WARNING: MiSTercade V1 mappings are deprecated."
            echo "A change to Jotego's JTFrame caused ghost inputs on V1.X boards."
            echo "Please consider updating to V1-2025 firmware."
            echo "See: https://misteraddons.com/blogs/news/mistercade-pre-order-firmware-update-and-pre-configured-input-mappings"
            echo ""
            read -p "Continue with V1 anyway? [y/N]: " v1_confirm < /dev/tty
            if [ "$v1_confirm" != "y" ] && [ "$v1_confirm" != "Y" ]; then
                echo "Exiting. Please update your firmware and re-run this script."
                exit 0
            fi
            ;;
        2) fw_prefix="v1_2025_" ;;
        3) fw_prefix="v2_" ;;
        4) fw_prefix="v3_" ;;
        *)
            echo "Invalid choice. Exiting."
            exit 1
            ;;
    esac
fi

# --- Step 2: Choose variant ---
echo ""
echo "Which mapping variant do you want?"
echo ""
echo "  1) Standard          - menu combo (Down+Start) enabled"
echo "  2) Freeplay          - menu combo enabled, start triggers coin"
echo "  3) No-Menu           - menu combo disabled (tournament mode)"
echo "  4) No-Menu Freeplay  - menu combo disabled, start triggers coin"
echo ""
read -p "Enter choice [1-4]: " variant_choice < /dev/tty

case "$variant_choice" in
    1) variant_suffix="mappings" ;;
    2) variant_suffix="freeplay_mappings" ;;
    3) variant_suffix="nomenu_mappings" ;;
    4) variant_suffix="nomenu_freeplay_mappings" ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

# Build the repo name
if [ -z "$fw_prefix" ]; then
    REPO_NAME="mistercade_${variant_suffix}"
else
    REPO_NAME="mistercade_${fw_prefix}${variant_suffix}"
fi

DB_URL="https://raw.githubusercontent.com/misteraddons/${REPO_NAME}/db/db.json.zip"

echo ""
echo "Selected: ${REPO_NAME}"
echo ""

# --- Step 3: Confirm ---
read -p "Apply this to ${DOWNLOADER_INI}? [y/N]: " confirm < /dev/tty
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "Cancelled."
    exit 0
fi

# End of interactive block
fi

# === Apply changes (shared by interactive and non-interactive modes) ===

# Create downloader.ini if it doesn't exist
if [ ! -f "$DOWNLOADER_INI" ]; then
    echo "Creating ${DOWNLOADER_INI}..."
    touch "$DOWNLOADER_INI"
fi

# Backup existing downloader.ini
BACKUP="${DOWNLOADER_INI}.bak"
cp "$DOWNLOADER_INI" "$BACKUP"
echo "Backed up to ${BACKUP}"

# Remove any existing mistercade mapping sections
TEMP_FILE=$(mktemp)

awk '
BEGIN { skip = 0 }
/^\[misteraddons\/mistercade_.*mappings\]/ { skip = 1; next }
skip && /^db_url[[:space:]]*=/ { skip = 0; next }
skip && /^\[/ { skip = 0 }
skip && /^[[:space:]]*$/ { next }
!skip { print }
' "$DOWNLOADER_INI" > "$TEMP_FILE"

# Remove trailing blank lines
sed -i -e :a -e '/^\n*$/{$d;N;ba' -e '}' "$TEMP_FILE" 2>/dev/null || true

# Append the new section
{
    echo ""
    echo "[misteraddons/${REPO_NAME}]"
    echo "db_url = ${DB_URL}"
} >> "$TEMP_FILE"

# Write back
cp "$TEMP_FILE" "$DOWNLOADER_INI"
rm -f "$TEMP_FILE"

echo ""
echo "Done! ${DOWNLOADER_INI} has been updated."
echo "  Repository: ${REPO_NAME}"
echo ""
echo "Run update_all or downloader to fetch your mappings."
echo ""
