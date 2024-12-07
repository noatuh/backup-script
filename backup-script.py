#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

# Define the source and destination directories
SOURCE_DIR = "/home/student/Downloads"
BACKUP_DIR = "/home/student/backup"

def create_backup():
    # Ensure the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Created backup directory: {BACKUP_DIR}")

    # Generate the timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_filename = f"logs_backup_{timestamp}.tar.gz"
    backup_filepath = os.path.join(BACKUP_DIR, backup_filename)

    try:
        # Create the backup using tar
        subprocess.run(["tar", "-czf", backup_filepath, "-C", SOURCE_DIR, "."], check=True)
        print(f"Backup created successfully: {backup_filepath}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create the backup. {e}")

def main():
    print("Starting backup process...")
    create_backup()
    print("Backup process completed.")

if __name__ == "__main__":
    main()
