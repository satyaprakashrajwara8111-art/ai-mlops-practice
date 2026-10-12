log_file = "system_monitor.log"

total_records = 0
normal_count = 0
alert_count = 0
highest_cpu = 0.0

print("=== Log Analyzer ===")

try:
    with open(log_file, "r") as file:
        for line in file:
            if "CPU:" not in line:
                continue

            total_records += 1

            if "Status: ALERT" in line:
                alert_count += 1
            elif "Status: NORMAL" in line:
                normal_count += 1

            try:
                cpu_part = line.split("CPU:")[1]
                cpu_value = float(cpu_part.split("%")[0].strip())

                if total_records == 1 or cpu_value > highest_cpu:
                    highest_cpu = cpu_value

            except (ValueError, IndexError):
                print("Skipping invalid log line:", line.strip())

    print("\n=== Monitoring Summary ===")
    print("Total records:", total_records)
    print("Normal records:", normal_count)
    print("Alert records:", alert_count)

    if total_records > 0:
        print("Highest CPU usage:", highest_cpu, "%")
    else:
        print("No valid monitoring records found.")

except FileNotFoundError:
    print("ERROR: Log file not found:", log_file)

print("Analysis finished.")