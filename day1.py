application = "Production App"
status= "Running"
cpu_usage = 65

print("AI + MLOps Trainning Started")
print("Application:", application)
print("Status:", status)
print("Cpu Usage:", cpu_usage, "%")

if cpu_usage > 80:
    print("ALERT: High CPU usage")
else:
    print("CPU Usage is normal")