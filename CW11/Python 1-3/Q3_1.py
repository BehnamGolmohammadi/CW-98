from datetime import datetime as dt

now = dt.now()
now = dt.strftime(now, "%Y.%m.%d %H:%M:%S")
now = dt.strptime(now, "%Y.%m.%d %H:%M:%S")

print(f"Current date and time: {now}")