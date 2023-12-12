import datetime
from playsound import playsound
import time

# Function to get alarm_hour
def get_alarm_hour():
    while True:
        try:
            alarm_hour = int(input("Enter alarm_hour (1-12): "))
            if 0 < alarm_hour <= 12:
                return alarm_hour
            else:
                print("Invalid alarm_hour. Enter a value between 1 and 12.\n")
        except ValueError:
            print("Error!")

# Function to get alarm_minute
def get_alarm_minute():
    while True:
        try:
            alarm_minute = int(input("Enter alarm_minute (0-59): "))
            if 0 <= alarm_minute <= 59:
                return alarm_minute
            else:
                print("Invalid alarm_minute. Enter a value between 0 and 59.\n")
        except ValueError:
            print("Error!")

# Function to get AM/PM
def get_am_pm():
    while True:
        try:
            am_pm = input("Enter AM or PM: ").lower()
            if am_pm == 'am' or am_pm == 'pm':
                return am_pm
            else:
                print("Invalid AM/PM indicator. Enter 'am' or 'pm'.\n")
        except ValueError:
            print("Error:")

# Function to set and play the alarm
def set_alarm():
    # Get alarm details from the user
    alarm_hour = get_alarm_hour()
    alarm_minute = get_alarm_minute()
    am_pm = get_am_pm()

    # Get current time
    current_time = datetime.datetime.now().time()

    # Calculate the alarm time
    alarm_time = datetime.time(
        hour=(alarm_hour + 12 if am_pm == 'pm' and alarm_hour != 12 else alarm_hour) % 24,minute=alarm_minute)

    # Calculate the time difference between current time and alarm time
    diff_time = datetime.datetime.combine(datetime.date.today(), alarm_time) - datetime.datetime.combine(datetime.date.today(), current_time)

    # Calculate the time to sleep before the alarm
    time_to_sleep = max(0, diff_time.total_seconds())

    # Sleep until it's time for the alarm
    if time_to_sleep > 0:
        time.sleep(time_to_sleep)

    # Display a message when it's time to wake up
    print("Time to wake up!")

    # Play the alarm sound
    play_alarm()

def play_alarm():
    # Play the alarm sound file
    playsound("A:\BCA PART-3\Project\Evolve Intern (Python)\Alarm Clock/alarm_clock.mp3")

# Call set_alarm to start the program
set_alarm()