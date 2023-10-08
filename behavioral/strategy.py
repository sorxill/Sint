from abc import ABCMeta, abstractclassmethod

class Sound(metaclass = ABCMeta):
    @abstractclassmethod
    def sound(self):
        pass

class CleanSound(Sound):
    def sound(self):
        print("Clean Sound")


class VintageSound(Sound):
    def sound(self):
        print("Vintage Sound")


class Synth(metaclass=ABCMeta):
    def __init__(self, soundSystem):
        self._soundSystem = soundSystem
    
    def playSound(self):
        self._soundSystem.sound()

    @property
    def soundSystem(self):
        return self._soundSystem
    
    @soundSystem.setter
    def soundSystem(self, soundSystem):
        self._soundSystem = soundSystem

class KeyScape(Synth):
    def __init__(self, cleanSound):
        self.cleanSound = cleanSound
        super().__init__(cleanSound)

class Melltron(Synth):
    def __init__(self, vintageSound):
        self.vintageSound = (vintageSound)
        super().__init__(vintageSound)