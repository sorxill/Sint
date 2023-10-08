from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow
import converterwindow
import decoratorwindow
import renderwindow

# Тут использовался singleton, гарантирует, что в приложении будет
#только один экземпляр класса Window

class Window(Tk, Singleton): 
    def init(self):
        super().__init__()

        self.button = Button(self, text="open eqs window", command=self.create_window_eqs)
        self.button.pack(expand=True) 

        self.button = Button(self, text="open footer", command=self.create_footer_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text="open converter", command=self.create_converter_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text="decorator", command=self.create_decorator)
        self.button.pack(expand=True)

        self.button = Button(self, text="render", command=self.create_render)
        self.button.pack(expand=True)


    def create_window_eqs(self):
            global extraWindow
            extraWindow = eqswindow.Extra()
    
    def create_footer_eqs(self):
            global extraWindow
            extraWindow = footerwindow.Extra()
    
    def create_converter_eqs(self):
            global extraWindow
            extraWindow = converterwindow.Extra()

    def create_decorator(self):
            global extraWindow
            extraWindow = decoratorwindow.Extra()
    
    def create_render(self):
            global extraWindow
            extraWindow = renderwindow.Extra()


    def __init__(self):
        pass