import pyautogui
import keyboard
from time import sleep, time
import math

sleep(4)

pyautogui.click(681, 389)
previous_time = 0
total = 0
x_end = 340
while not keyboard.is_pressed('q'):
    start_time = time()

    if math.floor(total) != previous_time:
        x_end += 3
        if x_end > 1360:
            x_end = 1360
        previous_time = math.floor(total)

    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()
    bg = pixels[655, 210]

    for i in range(x_end, 237, -1):
        if pixels[i, 402] != bg or pixels[i, 469] != bg:
            keyboard.press('space')
            break

    end_time = time() - start_time
    total += end_time
