from playsound import *
from _datetime import *


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Wrong format. Try again!'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Wrong hours format. Try again!'
        elif int(alarm_time[3:5]) > 59:
            return 'Wrong minutes format. Try again!'
        elif int(alarm_time[6:8]) > 59:
            return 'Wrong seconds format. Try again!'
        else:
            return 'Great'


while True:
    alarm_time = input('Enter time in that format: \'HH:MM:SS\'. \nTime of the alarmclock is: ')
    validate = validate_time(alarm_time)
    if validate != 'Great':
        print(validate)
    else:
        print(f'Alarmclock is set on time {alarm_time}.')
        break

alarm_hour = int(alarm_time[0:2])
alarm_minutes = int(alarm_time[3:5])
alarm_seconds = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_minutes = now.minute
    current_seconds = now.second

    if alarm_hour == current_hour:
        if alarm_minutes == current_minutes:
            if alarm_seconds == current_seconds:
                print('Get up!')
                playsound('C:/sport.mp3')
                break
