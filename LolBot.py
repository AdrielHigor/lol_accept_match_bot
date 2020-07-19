from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time

class Coordinates:
    def __init__(self):
        self.acceptBtn = (910,670)
        self.searchBtn = (880,780)
        self.textFld = (570,785)
        self.champSrch = (1100,315)
        self.champion = (760,365)
        self.confirmBtn = (960, 720)

class Commands:
    def __init__(self):
        self.coordinates = Coordinates()

    def champSearch(self, champ):
        auxiliar = 0
        if champ == '':
            pass
        else:
            while auxiliar != 5:
                auxiliar+=1
                pyautogui.doubleClick(self.coordinates.champSrch)
            pyautogui.typewrite(champ)
            time.sleep(1)
            pyautogui.click(self.coordinates.champion)
            time.sleep(1)
            pyautogui.click(self.coordinates.confirmBtn)

    def acceptButton(self):
        pyautogui.click(self.coordinates.acceptBtn)

    def searchButton(self):
        pyautogui.click(self.coordinates.searchBtn)

    def textField(self):
        pyautogui.click(self.coordinates.textFld)

    def selectLane(self, lane):
        if lane == 'None':
            pass
        else:
            pyautogui.typewrite(lane)
            pyautogui.press('enter')

    def imgGrab(self):
        box = (self.coordinates.acceptBtn[0]+20, self.coordinates.acceptBtn[1], self.coordinates.acceptBtn[0]+60, self.coordinates.acceptBtn[1]+30)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        if (a.sum()) != 0:
            print(a.sum())
        return (a.sum())




