import psutil
import time

print("=== Continuous System Monitoring ===")
print("Press Ctrl+C to stop monitoring.")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        print("\nCPU Usage:", cpu_usage, "%")
        print("Memory Usage:", memory_usage, "%")

        if cpu_usage >= 80:
            print("ALERT: High CPU usage!")

        if memory_usage >= 80:
            print("ALERT: High memory usage!")

        time.sleep(4)

except KeyboardInterrupt:
    print("\nMonitoring stopped safely.")