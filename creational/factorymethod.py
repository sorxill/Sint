from abc import ABCMeta, abstractclassmethod

# Фабричный метод - Это МЕТОД, порождает объект который нам нужен/указываем

class Plugin(metaclass=ABCMeta):
    @abstractclassmethod
    def type():
        raise NotImplementedError
    

class EffectPlugin(Plugin):
    def __init__(self):
        self.type = "Effect"
    
    def type(self):
        return self.type
    
class SynthPlugin(Plugin):
    def __init__(self):
        self.type = "Synth"

    def type(self):
        return self.type


class Creator:
    @staticmethod
    def Factory(type):
        if type == "Effect":
            return EffectPlugin()
        elif type == "Synth":
            return SynthPlugin()
        return None