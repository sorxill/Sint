class Enitity:
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        return self.sound
    

class EQ(Enitity):
    def __init__(self, eqed):
        self.eqed = eqed
    
    def play(self):
        return f"EQ[{self.eqed.play()}]"
    
class Compressor(Enitity):
    def __init__(self, compressed):
        self.compressed = compressed
    
    def play(self):
        return f"Compressor[{self.compressed.play()}]"