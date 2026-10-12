log_file = "app.log"

print("=== Safe Log Analyzer ===")

try:
    error_count = 0

    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())
                error_count += 1

    print("Total errors found:", error_count)

except FileNotFoundError:
    print("WARNING: Log file not found:", log_file)

except PermissionError:
    print("ERROR: Permission denied while reading log file")

print("Log analysis finished.")