import subprocess
import json
import time
import csv
from datetime import datetime

# --- Configuration ---
FILENAME = "wall_scan_data.csv"
SCAN_DURATION = 30  # How many seconds you want to sweep
SAMPLE_RATE = 0.2   # Time between samples (5 samples per second)

def get_wifi_rssi():
    try:
        res = subprocess.check_output(['termux-wifi-connectioninfo'])
        return json.loads(res).get('rssi')
    except:
        return None

print(f"--- READY TO SCAN ---")
print(f"1. Place ESP8266 on the other side of the wall.")
print(f"2. Press ENTER and move your phone slowly across the wall surface.")
input("Press Enter to start 30-second sweep...")

data_points = []
start_time = time.time()

try:
    while (time.time() - start_time) < SCAN_DURATION:
        rssi = get_wifi_rssi()
        if rssi:
            elapsed = round(time.time() - start_time, 2)
            data_points.append([elapsed, rssi])
            # Visual feedback: a simple bar
            bar = "#" * (abs(rssi) // 2)
            print(f"Time: {elapsed}s | Strength: {rssi} dBm | {bar}", end='\r')
        
        time.sleep(SAMPLE_RATE)

    # Save to CSV
    with open(FILENAME, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Time_Seconds", "RSSI_dBm"])
        writer.writerows(data_points)

    print(f"\n\n[SUCCESS] Scan saved to {FILENAME}")
    print("[*] Move this file to your Mac or use a Python Plotly script to view.")

except KeyboardInterrupt:
    print("\n[!] Scan aborted.")
