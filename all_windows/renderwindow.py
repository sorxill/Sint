from tkinter import *
from tkinter.messagebox import askquestion
from structural.facede import *


# Тут использовали паттерн Facade - заключается в том что нажав одну кнопку мы сразу
# поднимаем несколько различных методов

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Render window')
        self.geometry('200x780')

        self.button = Button(self, text="Start Rendering", command=self.start_rendering)
        self.button.pack(expand=True)

    def start_rendering(self):
        renderTrack = Render()
        askquestion("...", message="Start Rendering?")
        renderTrack.startrendering()