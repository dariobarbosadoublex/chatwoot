#!/usr/bin/env python3
import json
import os
import glob

def remove_powered_by_from_json_files():
    """Remove the POWERED_BY key from all JSON localization files"""

    # Widget localization files
    widget_files = glob.glob('app/javascript/widget/i18n/locale/*.json')

    # Survey localization files
    survey_files = glob.glob('app/javascript/survey/i18n/locale/*.json')

    # Dashboard localization files (BRANDING_TEXT)
    dashboard_files = glob.glob('app/javascript/dashboard/i18n/locale/*/inboxMgmt.json')

    all_files = widget_files + survey_files + dashboard_files

    for file_path in all_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Remove POWERED_BY from widget and survey files
            if 'POWERED_BY' in data:
                del data['POWERED_BY']
                print(f"Removed POWERED_BY from {file_path}")

            # Remove BRANDING_TEXT from dashboard files
            if 'INBOX_MGMT' in data and 'WIDGET_BUILDER' in data['INBOX_MGMT']:
                if 'BRANDING_TEXT' in data['INBOX_MGMT']['WIDGET_BUILDER']:
                    del data['INBOX_MGMT']['WIDGET_BUILDER']['BRANDING_TEXT']
                    print(f"Removed BRANDING_TEXT from {file_path}")

            # Write back the modified data
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    remove_powered_by_from_json_files()
