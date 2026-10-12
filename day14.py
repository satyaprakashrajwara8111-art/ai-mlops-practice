import json
import psutil
import time
from datetime import datetime

with open("config.json", "r") as file:
    config = json.load(file)

CPU_THRESHOLD = config["cpu_threshold"]
MEMORY_THRESHOLD = config["memory_threshold"]
INTERVAL = config["interval_seconds"]

print("=== Configurable System Monitor ===")
print("CPU threshold:", CPU_THRESHOLD, "%")
print("Memory threshold:", MEMORY_THRESHOLD, "%")
print("Interval:", INTERVAL, "seconds")
print("Press Ctrl+C to stop.")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        if cpu >= CPU_THRESHOLD or memory >= MEMORY_THRESHOLD:
            status = "ALERT"
        else:
            status = "NORMAL"

        print(
            f"{timestamp} | CPU: {cpu}% | "
            f"Memory: {memory}% | Status: {status}"
        )

        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nMonitoring stopped safely.")

except FileNotFoundError:
    print("config.json not found.")