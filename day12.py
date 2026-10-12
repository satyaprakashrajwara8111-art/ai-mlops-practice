import csv

log_file = "system_monitor.log"
csv_file = "monitor_report.csv"

try:
    with open(log_file, "r") as source, \
         open(csv_file, "w", newline="") as report:

        writer = csv.writer(report)

        writer.writerow([
            "Timestamp",
            "CPU",
            "Memory",
            "Status"
        ])

        count = 0

        for line in source:
            if "CPU:" not in line:
                continue

            parts = line.strip().split(" | ")

            timestamp = parts[0]
            cpu = parts[1].replace("CPU:", "").strip()
            memory = parts[2].replace("Memory:", "").strip()
            status = parts[3].replace("Status:", "").strip()

            writer.writerow([
                timestamp,
                cpu,
                memory,
                status
            ])

            count += 1

    print("CSV report created successfully!")
    print("Records exported:", count)
    print("File name:", csv_file)

except FileNotFoundError:
    print("Log file not found. Run day10.py first.")

except (IndexError, ValueError):
    print("Log format is incorrect. Check system_monitor.log.")