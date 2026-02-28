import os
import time
from datetime import date, datetime, timedelta, timezone

# os module:-
# print(os.getenv("RAM"))  # None
# print(os.getenv("RAM", "raja1634@"))  # raja1634@

# time module:-
# now = time.time()
# print(now)  # 1772219666.9514282, UTC time since Jan 1, 1970
# print("start")
# time.sleep(5)
# print("print after 5 seconds")

# datetime module:-
# now = datetime.now() # local time
# print(now)  # 2026-02-28 00:53:25.166438
# print(now.year)  # 2026
# print(now.month)  # 2
# print(now.day)  # 28
# print(now.hour)  # 0
# print(now.minute)  # 53
# print(now.second)  # 25
# d1 = datetime(2056, 12, 27, 14, 22, 44)
# print(d1)  # 2056-12-27 14:22:44
# diff = d1 - now
# print(diff)  # 11260 days, 13:08:14.363300
# print(diff.days)  # 11260
# print(diff.seconds)  # 47294
# print(diff.microseconds)  # 363300
# d2 = now + timedelta(days=23)
# print(d2)  # 2026-03-23 00:53:25.166438
# print(now.strftime("%d-%m-%y %H:%M:%S"))  # 28-02-26 01:22:32
# today = date.today()
# print(today)  # 2026-02-28
# print(today.year)  # 2026
# print(today.month)  # 2
# print(today.day)  # 28
# d1 = date(2024, 12, 30)
# print(d1)  # 2024-12-30
# d2 = date(2029, 2, 23)
# diff = d2 - d1
# print(diff)  # 1516 days, 0:00:00
# print(diff.days)  # 1516
# print(d2 + timedelta(hours=48))  # 2029-02-25
# print(d2 + timedelta(days=12)) # 2029-03-07
# print(today.strftime("%m-%d-%y"))  # 02-28-26
# now_ist = datetime.now()
# print(now_ist)  # 2026-02-28 01:35:24.928559
# now_utc = datetime.now(timezone.utc)
# print(now_utc)  # 2026-02-27 20:05:24.928786+00:00