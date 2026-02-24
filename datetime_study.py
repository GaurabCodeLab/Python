from datetime import date, datetime, timedelta, timezone
import time

# Getting Today's Date:-
# today = date.today()
# print(today)  # 2026-02-23
# print(today.year)  # 2026
# print(today.month)  # 2
# print(today.day)  # 23
# d = date(2024,12,31)
# print(d)  # 2024-12-31

# Getting Current Date & Time:-
# now = datetime.now()
# print(now)  # 2026-02-23 12:56:23.425138
# print(now.hour)  # 12
# print(now.minute)  # 56
# print(now.second)  # 23
# print(now.year)  # 2026
# print(now.month)  # 2
# print(now.day)  # 23
# dt = datetime(2024, 4, 25, 10, 55, 23)
# print(dt)  # 2024-04-25 10:55:23

# Formatting Date & Time:-
# now = datetime.now()
# print(now.strftime("%d-%m-%y %H:%M:%S"))  # 23-02-26 17:46:59
# print(now.strftime("%y-%m-%d %H")) # 26-02-23 17

now = datetime.now()
# print(now)  # 2026-02-24 01:52:37.978813
# print(now + timedelta(days=5))  # 2026-03-01 01:52:37.978813
# print(now - timedelta(hours=2))  # 2026-02-23 23:52:37.978813
# arguments of timedelta is days, hours, minutes, seconds and all are in floats

# Difference between two dates:-
# now = date.today()
# d1 = date(2024, 12, 31)
# diff = now - d1
# print(diff)  # 420 days, 0:00:00
# print(diff.days)  # 420
# now = datetime.now()
# d1 = datetime(2012, 12, 31, 13, 12, 33)
# diff = now - d1
# print(diff)  # 4802 days, 12:47:26.014105
# print(diff.days)  # 4802

# now_ist = datetime.now() # gives indian time
# now_utc = datetime.now(timezone.utc) # gives UTC time
# print(now_ist)  # 2026-02-24 02:04:14.163932
# print(now_utc)  # 2026-02-23 20:34:14.163956+00:00

# TIME MODULE:-

# current time in seconds:-
# now = time.time()  # Give seconds since 1 Jan 1970 (called Unix Timestamp)
# print(now)  # 1771917263.95265

# pause the program:-
# print("start")
# time.sleep(3)
# print("End after 3 seconds")