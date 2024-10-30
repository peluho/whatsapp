import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pygetwindow as gw  # Biblioteca para centrar el navegador

keyboard = Controller()

def send_whatsapp_message(msg: str):
    try:
        # Enviar mensaje con pywhatkit
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+34690629961",
            message=msg,
            tab_close=True
        )

        # Espera a que se cargue WhatsApp Web
        time.sleep(10)

        # Poner el navegador en primer plano
        browser_windows = [w for w in gw.getAllTitles() if "WhatsApp" in w or "Mozilla" in w or "Chrome" in w]
        if browser_windows:
            gw.getWindowsWithTitle(browser_windows[0])[0].activate()  # Activa la ventana del navegador

        # Simular clic y enviar mensaje
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message(msg="Test message from a Python script!")
