log_file = "app.log"

print("=== Application Log Analyzer ===")

error_count = 0

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
            error_count += 1

print("------------------------")
print("Total errors found:", error_count)