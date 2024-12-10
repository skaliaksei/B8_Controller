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

if __name__ == "__main__":
    time.sleep(1)  # Время, чтобы перейти к нужному окну
    activate_window("Air System - AnyDesk")  # Укажите заголовок окна, например, "Блокнот" для Notepad
    # activate_window("tst.txt")

    activate_login_window(135, 110, 140, 159)




    login(989, 549, 946, 576, "12345")
    # get_coordinates()
    # move_to_k7(857, 170)
    # stop_k7(234, 964)
    #
    # time.sleep(30)
    #
    # move_to_k7(857, 170)
    # auto_k7(251, 935)
    # move_to_main(561, 174)

    move_to_P8(1083, 132)
    start_P8(1240, 293)
    move_away(800, 600)
    time.sleep(10)
    #
    #
    stop_P8(1254, 318)
    move_to_main(561, 134)
    move_away(800, 750)

    activate_login_window(135, 110, 140, 159)

