import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

'''
Structure of the UI
-ExteriorGridLayout
  -TitleLabel
  -InteriorGridLayout
    -Button -Button
    -Button -Button
    -Button -Button
'''
class ButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super(ButtonGrid, self).__init__(**kwargs) #Used to initialize UI and **kwargs tells interpreter there can be multiple widgets
        self.cols = 1 #Refer to structure. ExteriorGridLayout has one column
        self.inside = GridLayout() #Initializing InteriorGridLayout
        self.inside.cols = 2 #Refer to structure. InteriorGridLayout has two columns
        #--------ExteriorGridLayout Begins--------#
        
        #--------TITLE LABEL--------#
        
        #self.title = Label(text="Follow @thiru.jpg")
        #self.add_widget(self.title)
        
        #--------InteriorGridLayout Begins--------#
        
        #--------1st Row of Buttons--------#
        
        self.but1 = Button(text="1")
        self.but1.bind(on_press=self.b1)
        self.inside.add_widget(self.but1)
        
        self.but2 = Button(text="2")
        self.but2.bind(on_press=self.b2)
        self.inside.add_widget(self.but2)
        
        #--------2nd Row of Buttons--------#
        
        self.but3 = Button(text="3")
        self.but3.bind(on_press=self.b3)
        self.inside.add_widget(self.but3)
        
        self.but4 = Button(text="4")
        self.but4.bind(on_press=self.b4)
        self.inside.add_widget(self.but4)
        
        #--------3rd Row of Buttons--------#
        
        self.but5 = Button(text="5")
        self.but5.bind(on_press=self.b5)
        self.inside.add_widget(self.but5)
        
        self.but6 = Button(text="6")
        self.but6.bind(on_press=self.b6)
        self.inside.add_widget(self.but6)
        
        #--------InteriorGridLayout Ends--------#
        
        self.add_widget(self.inside)#Adding Interior Grid to Exterior Grid
        
        #--------ExteriorGridLayout Ends--------#
        
    def b1(self, instance):
        print("1 pressed")
    def b2(self, instance):
        print("2 pressed")
    def b3(self, instance):
        print("3 pressed")
    def b4(self, instance):
        print("4 pressed")
    def b5(self, instance):
        print("5 pressed")
    def b6(self, instance):
        print("6 pressed")

class DocScanApp(App):
    def build(self):
       return ButtonGrid()        

if __name__ == "__main__":
    DocScanApp().run()