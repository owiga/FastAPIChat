import time
import psutil




while True:
    info = {}
    try:
        p = psutil.cpu_percent(interval=None)
        m = psutil.virtual_memory().percent

        info["CPU"] = info.get("CPU", p)
        info["RAM"] = info.get("RAM", m)

        print(info)

        time.sleep(1)
    except KeyboardInterrupt:
        break
