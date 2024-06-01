from typing import List
from src.main.components.component import Component


class Plugboard(Component):
    def __init__(self, pairs: dict):
        super().__init__()
        self.right = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for k, v in pairs.items():
            self.right = self.right[:self.right.find(k)] + v + self.right[self.right.find(k) + 1:]
            self.right = self.right[:self.left.find(v)] + k + self.right[self.left.find(v) + 1:]
