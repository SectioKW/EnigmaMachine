from typing import List
from src.main.feature.enigma import Enigma
from src.main.utilities.Visual import Visual


class EnigmaVisual(Enigma):

    def encrypt_signal(self, letter: str):
        path = []
        self.rotate_rotors()
        signal = self.kb.forward(letter)
        path.append(signal)
        path.append(signal)
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        for ro in reversed(self.rotors):
            signal = ro.forward(signal)
            path.append(signal)
            path.append(signal)
        signal = self.reflector.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        for ro in self.rotors:
            signal = ro.backward(signal)
            path.append(signal)
            path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.kb.backward(signal)

        return path, letter

    def start(self):
        components = [self.kb, self.pb]
        for ro in reversed(self.rotors):
            components.append(ro)
        components.append(self.reflector)
        visual = Visual(components,self)
        visual.start()


test = EnigmaVisual()
test.start()
