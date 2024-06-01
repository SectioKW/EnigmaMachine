from typing import List


class Component:
    def __init__(self):
        self.right = None
        self.left = None

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
