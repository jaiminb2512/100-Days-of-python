# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications

import time
from plyer import notification

def drink_water():
    while True:
        # Display a notification to remind you to drink water
        notification.notify(
            title='Drink Water Reminder',
            message='It\'s time to drink some water!',
            app_name='Water Reminder',
            timeout=10
        )
        
        # Wait for 2 hours
        time.sleep(2 * 60 * 60)

if __name__ == "__main__":
    drink_water()
