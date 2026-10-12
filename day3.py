applications = [
    {"name": "Payment App", "cpu": 45},
    {"name": "Login App", "cpu": 55},
    {"name": "Shopping App", "cpu": 65},
    {"name": "Database App", "cpu": 98},
    {"name": "Web App", "cpu": 30}
]

print("=== Production Application Monitoring ===")

for app in applications:
    print("\nApplication:", app["name"])
    print("CPU Usage:", app["cpu"], "%")

    if app["cpu"] >= 80:
        print("Status: ALERT - High CPU usage!")
    else:
        print("Status: NORMAL")