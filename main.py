import pyautogui as auto
from PIL import ImageGrab
import time

# def bbox():
#     time.sleep(3)
#     screen = ImageGrab.grab(bbox=(200, 600, 500, 800))
#     screen.show()
#     print(screen.getcolors())
# bbox()


def jump():
    auto.press('space')

def main():
    time.sleep(3)
    while True:
        screen = ImageGrab.grab(bbox=(190, 600, 500, 800)) 
        for color in screen.getcolors():
            if color[0] > 2400: 
                if color[1] == (83, 83, 83) or color[1] == (172, 172, 172):
                    jump()
                    break

if __name__ == "__main__":
    main()