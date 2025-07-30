import time
import sys

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write('\r' + timer)
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    print("\nTime is up!!!")

try:
    t = int(input("Enter time in seconds: "))
    countdown(t)
except ValueError:
    print("Invalid value")