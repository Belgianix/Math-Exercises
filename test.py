import threading
import time

def countdown_timer(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'{mins:1.1f}:{secs:1.1f}'
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown_timer(5)


