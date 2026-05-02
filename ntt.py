#!/usr/bin/env python3
"""
Smartwatch Application Installer (Terminal Version)
Simulates installing an app on a connected smartwatch via CLI.
"""

import time
import sys

def terminal_installer(app_name, watch_ip="192.168.1.100"):
    print(f" Smartwatch App Installer")
    print(f" Target watch: {watch_ip}")
    print(f" App: {app_name}\n")

    steps = [
        ("Connecting to smartwatch", 1),
        ("Authenticating device", 1),
        ("Checking storage space", 0.8),
        ("Uploading app bundle", 1.5),
        ("Installing dependencies", 1.2),
        ("Setting permissions (HR, GPS, Notifications)", 1),
        ("Optimizing for battery life", 0.7),
        ("Finalizing installation", 0.5)
    ]

    for step, duration in steps:
        print(f" {step}...", end=" ", flush=True)
        time.sleep(duration)
        print("✓")

    print("\n Installation complete!")
    print(f" {app_name} is now ready on your smartwatch.\n")

    # Simulate quick uninstall option
    choice = input("Do you want to uninstall the app? (y/n): ").strip().lower()
    if choice == 'y':
        print("\n Uninstalling...")
        time.sleep(1)
        print(f" {app_name} has been removed from the watch.")
    else:
        print(" Keeping app installed. Exiting installer.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = " ".join(sys.argv[1:])
    else:
        app = input("Enter smartwatch app name: ").strip()
        if not app:
            app = "HealthTracker"
    terminal_installer(app)