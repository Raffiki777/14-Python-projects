import time

def digital_clock(set_alarm):

    print("__TIC-TOC__")
    print()
    for x in range(set_alarm, 0, -1):  # For x in range of set_alarm time in reverse
        seconds = x % 60  # Use modulus to get remainder, to not extend 60
        minutes = int(x / 60) % 60  # 60 seconds in a minute
        hours = int(x / 3600)  # 3600 seconds in an hour
        print(f"{hours:02}:{minutes:02}:{seconds:02}")  # 02 for zero padding
        time.sleep(1)

    print("Wake Up!")

digital_clock(set_alarm = 5)