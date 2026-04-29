# MiSTercade Mapping Updater
This database can be integrated in MiSTer FPGA by editing the `downloader.ini` file at the root of the SD. 

This mapping has Down + Start hardcoded for the OSD menu combo. If you prefer not to use Down + Start, you'll want to avoid using the preset mapping repositories. You can always copy and paste mappings, or create the mappings by hand.

For tournaments, please manage your mappings manually (either copy and paste the indiviaul mapping files, or manually map games). This will avoid players accidentally pressing Down + Start during gameplay. Thanks!

## How to Integrate the Mappings into MiSTer Downloader:
To integrate it in a MiSTer device, add the following section to the end of to the file `downloader.ini` that should be placed at the root of the SD (if it doesn't exist, you may create it for this purpose):
```ini
[misteraddons/mistercade_v2_freeplay_mappings]
db_url = https://raw.githubusercontent.com/misteraddons/mistercade_v2_freeplay_mappings/db/db.json.zip
```
After that, run *downloader* or *update_all* as usual. It will try to fetch the files from your newly created database. 

## To Do
Handle twin stick mappings (not currently available on V2)

## Non-free-play Mapping Repository
If you want to try the normal mapping repository (no freeplay), go here: https://github.com/misteraddons/mistercade_v2_mappings
