import subprocess
import json
import time
import os

# Baseline is the 'clear' room signal strength
BASELINE = -40 
SENSITIVITY = 5 # dBm drop to trigger 'Visual'

def get_signal():
    try:
        res = subprocess.check_output(['termux-wifi-connectioninfo'])
        return json.loads(res).get('rssi')
    except: return None

def visualize_shadow(rssi):
    # Calculate how much signal is blocked
    diff = abs(rssi - BASELINE)
    
    # Create a visual 'Density' bar
    # More '#' means more 'Matter' is blocking the signal
    density = int(diff / 2)
    display = "#" * density + "." * (20 - density)
    
    if diff > SENSITIVITY:
        return f"[{display}] OBJECT DETECTED"
    return f"[{display}] CLEAR"

print("--- WI-FI WALL-SCANNER ACTIVE ---")
while True:
    r = get_signal()
    if r:
        print(visualize_shadow(r), end='\r')
    time.sleep(0.1) # High sample rate for 'Vision'
