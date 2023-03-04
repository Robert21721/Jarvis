import time
from pymongo import MongoClient
from pywhatkit.core import core
import webbrowser as web
from urllib.parse import quote
import pyautogui as pg


def sendwhatmsg_instantly(
        phone_no: str,
        message: str,
        tab_close: bool = False,
        close_time: int = 3,
    ) -> None:

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(7)
    pg.press("enter")
    if tab_close:
        core.close_tab(wait_time=close_time)

def WhatsApp_Messages(name, message):

    CONNECTION_STRING = "mongodb+srv://Meow:Fortissimo21@cluster0.lsv82vu.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)
    print("Connection Successful")

    JarvisDB = client["JarvisDB"]
    contacts = JarvisDB["contacts"]

    for x in contacts.find():
        if (x["name"] == name):
            phone_number = x["phone_nr"]
            sendwhatmsg_instantly(f"{phone_number}", f"{message}")
            break

    client.close()



# def WhatsApp_Call(name):

#     position = pt.locateCenterOnScreen("photos/start.png", confidence=.7)
#     x = position[0]
#     y = position[1]
#     pt.moveTo(x, y, duration = 0.5)
#     pt.click()
#     sleep(0.1)

#     position = pt.locateCenterOnScreen("photos/whatsapp_start.png", confidence=.7)
#     x = position[0]
#     y = position[1]
#     pt.moveTo(x, y, duration = 0.5)
#     pt.click()
#     sleep(7)

#     position = pt.locateCenterOnScreen("photos/" + name +".png", confidence=.9)
#     x = position[0]
#     y = position[1]
#     pt.moveTo(x, y, duration = 0.5)
#     pt.click()
#     sleep(0.5)

#     position = pt.locateCenterOnScreen("photos/call.png", confidence=.7)
#     x = position[0]
#     y = position[1]
#     pt.moveTo(x + 20, y, duration = 0.5)
#     pt.click()
