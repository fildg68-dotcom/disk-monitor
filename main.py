import shutil
import time
from datetime import datetime
previous_status = None

while True:

    print("Час перевірки:", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    disk = shutil.disk_usage("/")
    total = disk.total / (1024 * 1024 * 1024)
    used = disk.used / (1024 * 1024 * 1024)
    free = disk.free / (1024 * 1024 * 1024)
    usage_percent = used / (used + free) * 100
    current_status = usage_percent >= 90
    print("Загалом місця:",round(total, 2), "GiB")
    print("Використовується:", round(used, 2),"GiB")
    print("Вільно:", round(free, 2), "GiB")
    print("Заповнення: ", (round(usage_percent, 1)))
    if current_status != previous_status:
        if current_status :
            message = "Місця на диску критично мало"
        else:
            message = "Місця на диску достатньо"
        print(message)
        with open("events.log", "a", encoding="utf-8") as file:
            file.write(datetime.now().strftime("%d.%m.%Y %H:%M:%S | ") + message + "\n")
    previous_status = current_status
    time.sleep(120)




