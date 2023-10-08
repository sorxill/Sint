from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow
import converterwindow
import decoratorwindow
import renderwindow
import iteratorwindow
import groupwindow
import strategywindow

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

        self.button = Button(self, text="iterator", command=self.create_iterator)
        self.button.pack(expand=True)

        self.button = Button(self, text="Group", command=self.create_group)
        self.button.pack(expand=True)

        self.button = Button(self, text="Strategy", command=self.create_strategy)
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

    def create_iterator(self):
            global extraWindow
            extraWindow = iteratorwindow.Extra()
        
    def create_group(self):
            global extraWindow
            extraWindow = groupwindow.Extra()

    def create_strategy(self):
            global extraWindow
            extraWindow = strategywindow.Extra()


    def __init__(self):
        pass