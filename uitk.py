from tkinter import *
from picamera import PiCamera
import time

camera = PiCamera()
camera.color_effects = (128,128)
app = Tk()

def takePicture():
    timestamp = int(time.time())
    camera.capture("/home/pi/Desktop/Actual Project/Scans/"+str(timestamp)+".jpg")
    print(timestamp)

top = Frame(app)
bottom = Frame(app)
top.pack()
bottom.pack(side=BOTTOM)
appName = Label(top,text="Document Scanner")
scanButton = Button(bottom, text = "Scan Document", command=takePicture)
appName.pack()
scanButton.pack()