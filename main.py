import shutil
import time

while True:
    disk = shutil.disk_usage("/")
    total = disk.total / (1024 * 1024 * 1024)
    used = disk.used / (1024 * 1024 * 1024)
    free = disk.free / (1024 * 1024 * 1024)
    usage_percent = used / (used + free) * 100
    print("Загалом місця",round(total, 2), "GiB")
    print("Використовується", round(used, 2),"GiB")
    print("Вільно", round(free, 2), "GiB")
    print("Заповнення: ", (round(usage_percent, 1)))
    if usage_percent < 90:
        print("Місця на диску достатньо")
    else:
        print("Місця на диску критично мало")
    time.sleep(120)



