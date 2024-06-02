from typing import List
from src.main.utilities.KeyReader import KeyReader
from src.main.components import keyboard, plugboard, reflector, rotor


class Enigma:
    def __init__(self):
        self.Key = KeyReader()
        self.kb = keyboard.Keyboard()
        self.pb = self.load_plugboard()
        self.rotors = self.load_rotors()
        self.set_ring_setting()
        self.set_rotor_start()
        self.reflector = self.load_reflector()

    def load_plugboard(self) -> object:
        return plugboard.Plugboard(self.Key.get_plugboard())

    def load_rotors(self) -> List[object]:
        rotors = []
        data = self.Key.get_rotors()
        for ro in data:
            rotors.append(rotor.Rotor(data[ro]['wiring'], data[ro]['notch']))
        return rotors

    def load_reflector(self) -> object:
        key = self.Key.get_reflector()
        return reflector.Reflector(self.Key.get_reflectors()[key])

    def set_rotor_start(self):
        start = self.Key.get_rotor_start()
        for i, ro in enumerate(self.rotors):
            ro.rotate_to_letter(start[i])

    def set_ring_setting(self):
        setting = self.Key.get_ring_setting()
        for i, ro in enumerate(self.rotors):
            ro.set_ring(setting[i])

    def rotate_rotors(self):
        r3 = self.rotors[2]
        r2 = self.rotors[1]
        r1 = self.rotors[0]
        if r2.notch == r2.left[0] and r3.notch == r3.left[0]:
            r3.rotate()
            r2.rotate()
            r1.rotate()
        # Double step
        elif r2.notch == r2.left[0]:
            r3.rotate()
            r2.rotate()
            r1.rotate()
        elif r3.notch == r3.left[0]:
            r3.rotate()
            r2.rotate()
        else:
            r3.rotate()

    def encrypt_signal(self, letter: str) -> str:
        self.rotate_rotors()
        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        for ro in reversed(self.rotors):
            signal = ro.forward(signal)
        signal = self.reflector.reflect(signal)
        for ro in self.rotors:
            signal = ro.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)
        return letter

    def encrypt_message(self, message: str) -> str:
        encrypted_message = ''
        for letter in message:
            if letter == ' ':
                encrypted_message += ' '
            else: encrypted_message += self.encrypt_signal(letter)
        print(f'Original message: {message}')
        print(f'Encrypted message: {encrypted_message}')
        return encrypted_message

    def decrypt_signal(self, letter: str) -> str:
        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        for ro in self.rotors:
            signal = ro.forward(signal)
        signal = self.reflector.reflect(signal)
        for ro in reversed(self.rotors):
            signal = ro.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)
        return letter




