import logging
import psutil
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "day16_monitor.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ],
    force=True
)

logging.info("System health check started")

try:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    logging.info("Timestamp: %s", datetime.now())
    logging.info("CPU usage: %.1f%%", cpu)
    logging.info("Memory usage: %.1f%%", memory)

    if cpu >= 50 or memory >= 50:
        logging.warning("High CPU or memory usage detected")
    else:
        logging.info("System status: NORMAL")

except Exception:
    logging.exception("System health check failed")

finally:
    logging.info("System health check finished")