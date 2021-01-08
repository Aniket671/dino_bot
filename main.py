import pyautogui
from PIL import ImageGrab
import time

def TakeScreenshoot():
    image = ImageGrab.grab().convert('L')
    return image

def botDay():
    for i in range(175, 225):
        for j in range(300, 418):
            if data[i, j] > 100:
                return True

def botNight():
    for i in range(175, 225):
        for j in range(300, 418):
            if data[i, j] < 100:
                return True

def bird():
    for i in range(190, 295):
        for j in range(420, 500):
            if data[i, j] > 100:
                hit("up")
                return True

def cactus():
    for i in range(190, 290):
        for j in range(420, 500):
            if data[i, j] < 100:
                hit("up")
                return True

def bott(data):
    if botDay() and cactus:
        cactus()
    elif botNight() and bird:
        bird()

'''
def collide(data):
#bird
    for i in range(175, 225):
        for j in range(300, 418):
            if data[i, j] < 100:
                hit("down")
                back()
                return                              #Thia Code Didn't Work :(
#dino
    for i in range(200, 255):
        for j in range(418, 505):
            if data[i,j] < 100:
                hit("up")
                return
    return
'''

def hit(key):
    pyautogui.keyDown(key)
    return

if __name__ == '__main__':
    print("dino game going to start in 3 sec...")
    time.sleep(2)
    hit("space")
    while True:
        image = TakeScreenshoot()
        data = image.load()
        bott(data)


'''
        for i in range(175, 295):
            for j in range(420, 500):
                data[i, j] = 71              #for checking rectangle of that dino-soroussssssss


        #for i in range(175,225):
        #    for j in range(300, 418):
        #        data[i, j] = 171

            image.show()
            break
'''