from src.main.components.component import Component


class Reflector(Component):
    def __init__(self, wiring: str, notch: int = 0):
        super().__init__()
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.right = wiring
        self.notch = notch

    def reflect(self, signal):
        return self.forward(signal)
