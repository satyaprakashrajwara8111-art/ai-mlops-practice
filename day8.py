import psutil

print("=== Real System Monitoring ===")

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent

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