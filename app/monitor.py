
import psutil
from datetime import datetime


def get_system_status():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    if cpu >= 80 or memory >= 80:
        status = "ALERT"
    else:
        status = "NORMAL"

    return {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "cpu": cpu,
        "memory": memory,
        "status": status,
    }


if __name__ == "__main__":
    result = get_system_status()

    print("=== System Health Report ===")
    print("Timestamp:", result["timestamp"])
    print("CPU:", result["cpu"], "%")
    print("Memory:", result["memory"], "%")
    print("Status:", result["status"])
