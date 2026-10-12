import psutil
import time
from datetime import datetime

log_file = "system_monitor.log"

print("=== System Monitoring with Logging ===")
print("Press Ctrl+C to stop.")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if cpu >= 80 or memory >= 80:
            status = "ALERT"
        else:
            status = "NORMAL"

        log_message = (
            f"{timestamp} | CPU: {cpu}% | "
            f"Memory: {memory}% | Status: {status}"
        )

        print(log_message)

        with open(log_file, "a") as file:
            file.write(log_message + "\n")

        time.sleep(4)

except KeyboardInterrupt:
    print("\nMonitoring stopped safely.")
    print("Results saved in:", log_file)    