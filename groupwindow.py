from tkinter import *
from behavioral.observer import *


# Observer - уведомление "подписанных" на этот класс об изменениях в классе

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Sampler')
        self.geometry('640x480')

        self.compressor = Compressor("Compresspr")
        self.kick = Kick()

        l = Label(self, text="Change Gain of the %s" % self.kick.name)
        l.pack()

        scale = Scale(self, command=lambda value: self.change_gain(int(value)), from_=0, to=100)
        scale.pack()

    def change_gain(self, gain):
        self.compressor.attach(self.kick)
        self.compressor.setGain = gain