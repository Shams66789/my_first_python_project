import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please drink water!!",
            message = "You have not drink water for an hour. Drink now and take a rest from your work for a while.",
            #app_icon = "pictures\icon.ico",
            timeout = 10
        )
        time.sleep(60*60)
