from bs4 import BeautifulSoup
import cv2
import pyautogui
import easyocr
image = pyautogui.screenshot("test.png")

imagepath = 'test.png'

read = cv2.imread(imagepath)

reader = easyocr.Reader(['en'], gpu=False)

text = reader.readtext('test.png', detail = 0)

file = open("test.txt", "w")
file.write(text)
file.close()
