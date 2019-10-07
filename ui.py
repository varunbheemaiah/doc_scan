from kivy.app import App
from kivy.uix.button import Button
from picamera import PiCamera
import time

camera = PiCamera()

class TestApp(App):
    def takePicture(self,arg):
        timestamp = int(time.time())
        camera.capture("/home/pi/Desktop/Actual Project/Scans/"+str(timestamp)+".jpg")
    def build(self):
        scanButton = Button(text="Scan Document", pos=(300,350), size_hint = (.25, .18), font_size="20")
        scanButton.bind(on_press=self.takePicture)
        return scanButton
        
TestApp().run()