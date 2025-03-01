import time
import pyautogui
import pydirectinput

#pydirectinput

def move_forward(sec):
    pyautogui.keyDown('w')
    time.sleep(sec)
    pyautogui.keyUp('w')

def move_backward(sec):
    pyautogui.keyDown('s')
    time.sleep(sec)
    pyautogui.keyUp('s')

def move_left(sec):
    pyautogui.keyDown('a')
    time.sleep(sec)
    pyautogui.keyUp('a')

def move_right(sec):
    pyautogui.keyDown('d')
    time.sleep(sec)
    pyautogui.keyUp('d')

def jump():
    pyautogui.press('space')

def aim(x, y):
    pydirectinput.moveRel(x, y)

def shoot(sec):
    pydirectinput.mouseDown()
    time.sleep(sec)
    pydirectinput.mouseUp()

def takeAim(sec):
    pydirectinput.mouseDown(button='right')
    time.sleep(sec)
    pydirectinput.mouseUp(button='right')

def inventory():
    pydirectinput.press('tab')

def close():
    pydirectinput.press('esc')

def crouch(sec):
    pydirectinput.keyDown('ctrl')
    time.sleep(sec)
    pydirectinput.keyUp('ctrl')

def sprint(sec):
    pydirectinput.keyDown('shift')
    time.sleep(sec)
    pydirectinput.keyUp('shift')

def shoot(sec):
    pydirectinput.mouseDown(button='left')
    time.sleep(sec)
    pydirectinput.mouseUp(button='left')

def reload():
    pyautogui.press('r')

def interact():
    pyautogui.press('e')

def use_item():
    pyautogui.press('f')

class slots():
    def slot1():
        pydirectinput.press('1')
    def slot2():
        pydirectinput.press('2')
    def slot3():
        pydirectinput.press('3')
    def slot4():
        pydirectinput.press('4')
    def slot5():
        pydirectinput.press('5')
    def slot6():
        pydirectinput.press('6')