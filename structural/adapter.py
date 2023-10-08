from abc import ABC, abstractclassmethod

# Используем Adapter - преобразование из аудио в миди,
# мы все так же продолжаем проигрывать аудио, но суем вместо аудио уже конвертированный миди

class Audio(ABC):
    @abstractclassmethod
    def audioRecord():
        pass

class Midi(ABC):
    @abstractclassmethod
    def midiTrack():
        pass

class AudioTrack(Audio):
    def audioRecord(self):
        print("Audio is playing..")

class MidiTrack(Midi):
    def midiTrack(self):
        print("Midi is playing..")


class AudioMidiAdapter(Audio):
    def __init__(self):
        self.midi = MidiTrack()
    
    def audioRecord(self):
        self.midi.midiTrack()