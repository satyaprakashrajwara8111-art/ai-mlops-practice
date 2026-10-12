import psutil
import csv
import time
from datetime import datetime

csv_file = "automated_monitor_report.csv"

try:
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Timestamp",
                "CPU",
                "Memory",
                "Status"
            ])

        print("Automated monitoring started.")
        print("Press Ctrl+C in the Terminal to stop.")

        while True:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            status = (
                "ALERT"
                if cpu >= 80 or memory >= 80
                else "NORMAL"
            )

            writer.writerow([
                timestamp,
                cpu,
                memory,
                status
            ])
            file.flush()

            print(
                f"{timestamp} | CPU: {cpu}% | "
                f"Memory: {memory}% | Status: {status}"
            )

            time.sleep(4)

except KeyboardInterrupt:
    print("\nMonitoring stopped safely.")
    print("Report saved to:", csv_file)