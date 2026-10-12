application = "Production App"
environment = "PROD"

cpu_usage = 40
memory_usage = 85

print("=== Application Health Check ===")
print("Application:", application)
print("Environment:", environment)
print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory_usage, "%")

if cpu_usage >= 80:
    print("ALERT: High CPU usage!")
else:
    print("CPU status: NORMAL")

if memory_usage >= 80:
    print("ALERT: High memory usage!")
else:
    print("Memory status: NORMAL")