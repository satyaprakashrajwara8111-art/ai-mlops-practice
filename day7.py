log_file = "app.log"

error_count = 0
warning_count = 0
info_count = 0

print("=== DevOps Log Monitoring Tool ===")

try:
    with open(log_file, "r") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                print("ERROR DETECTED:", line)
                error_count += 1

            elif "WARNING" in line:
                print("WARNING DETECTED:", line)
                warning_count += 1

            elif "INFO" in line:
                info_count += 1

    print("\n=== Monitoring Summary ===")
    print("Total errors:", error_count)
    print("Total warnings:", warning_count)
    print("Total info messages:", info_count)

    if error_count > 0:
        print("Overall status: ATTENTION REQUIRED")
    else:
        print("Overall status: HEALTHY")

except FileNotFoundError:
    print("ERROR: Log file not found:", log_file)

except PermissionError:
    print("ERROR: Permission denied.")

print("Monitoring script finished.")