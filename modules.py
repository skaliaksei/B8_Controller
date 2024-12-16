import pyautogui
import pygetwindow as gw
# from pynput.mouse import Controller, Button
import time

# Работаем с открытием окна
def activate_window(window_title):
    # Найти окно по его заголовку
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        # Восстановить окно, если оно свернуто
        if not window.isMaximized and not window.isActive:
            window.restore()
        # Активировать окно
        window.activate()
    else:
        print(f"Окно с заголовком '{window_title}' не найдено.")

def activate_login_window(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1, duration=0.01)
    pyautogui.click()
    pyautogui.moveTo(x2, y2, duration=0.01)
    pyautogui.click()
    time.sleep(0.1)

def get_coordinates():
    time.sleep(3)
    print(pyautogui.position())

def move_away(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    time.sleep(0.5)

def login(x1, y1, x2, y2, password):
    pyautogui.moveTo(x1, y1, duration=0.01)
    pyautogui.click()
    pyautogui.typewrite(password, interval=0.005)
    pyautogui.moveTo(x2, y2, duration=0.01)
    pyautogui.click()

def move_to_main(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    print('Moved to Main Menu')
    pyautogui.click()
    print('Entered to Main Menu')

def move_to_k7(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    print('Moved to K7')
    pyautogui.click()
    print('Entered to Menu')

def stop_k7(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    pyautogui.click()
    print("Stopped K7")
    time.sleep(3)

def auto_k7(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    pyautogui.click()
    print("Auto K7")
    time.sleep(3)

def move_to_P8(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    pyautogui.click()
    time.sleep(1)

def stop_P8(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    pyautogui.click()
    print("Stopped V8")
    time.sleep(3)

def start_P8(x, y):
    pyautogui.moveTo(x, y, duration=0.01)
    pyautogui.click()
    print("Start V8")
    time.sleep(3)
