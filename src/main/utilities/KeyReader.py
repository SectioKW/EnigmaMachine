import json
import os


class KeyReader:
    def __init__(self):
        self.file = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'keySetting.json')
        self.keys = self.read_keys()

    def read_keys(self):
        with open(self.file, 'r') as f:
            keys = json.load(f)
        return keys

    def get_plugboard(self):
        return self.keys['plugboard']

    def get_rotors(self):
        order = self.keys['rotorOrder']
        rotors = self.keys['rotors']
        data = {}
        for ro in order:
            data[ro] = rotors[ro]
        return data

    def get_reflectors(self):
        return self.keys['reflectors']

    def get_reflector(self):
        return self.keys['reflector']

    def get_rotor_start(self):
        return self.keys['initialPositions']

    def get_ring_setting(self):
        return self.keys['ringSettings']
