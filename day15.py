import argparse
import psutil
from datetime import datetime

parser = argparse.ArgumentParser(
    description="System CPU and memory checker"
)

parser.add_argument(
    "--cpu",
    type=float,
    default=80,
    help="CPU alert threshold (default: 80)"
)

parser.add_argument(
    "--memory",
    type=float,
    default=80,
    help="Memory alert threshold (default: 80)"
)

args = parser.parse_args()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("=== System Health Check ===")
print("Time:", timestamp)
print("CPU usage:", cpu, "%")
print("Memory usage:", memory, "%")

if cpu >= args.cpu or memory >= args.memory:
    print("Status: ALERT")
else:
    print("Status: NORMAL")

print("CPU threshold:", args.cpu, "%")
print("Memory threshold:", args.memory, "%")