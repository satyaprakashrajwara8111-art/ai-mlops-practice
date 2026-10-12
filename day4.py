def check_cpu(application_name, cpu_usage):
    print("Application:", application_name)
    print("CPU Usage:", cpu_usage, "%")

    if cpu_usage > 75:
        print("Status:ALERT - High CPU usage!")
    else:
        print("Status: NORMAL")
    print("--------------------------------------------------") 

print("=== Production Monitoring ===")

check_cpu("Payment App", 90)
check_cpu("Login App", 85)
check_cpu("Database App", 92)
check_cpu("Web App", 30)
check_cpu("API Gateway", 88)