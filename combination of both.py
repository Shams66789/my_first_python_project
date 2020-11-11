import time
from plyer import notification
import PyPDF2
import pyttsx3

if __name__ == '__main__':
    pdf = pyttsx3.init()
    while True:
        notification.notify(
            title = "Please drink water!!",
            message = "You have not drink water for an hour. Drink now and take a rest from your work for a while.",
            #app_icon = "pictures\icon.ico",
            timeout = 10,
        )
    
        gib = "Please drink water!! You have not drink water for an hour. Drink now and take a rest from your work for a while."
        pdf.say(gib)
        pdf.runAndWait()

        time.sleep(30)