from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(total_seconds):
    seconds_passed = 0

    print(CLEAR)
    while seconds_passed < total_seconds:
        time.sleep(1)
        seconds_passed += 1

        time_left = total_seconds - seconds_passed
        minutes_left = time_left // 60  
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}ALARM WILL SOUND IN {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds 
alarm(total_seconds)

