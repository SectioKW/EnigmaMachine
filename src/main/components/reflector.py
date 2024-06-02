from src.main.components.component import Component


class Reflector(Component):
    def __init__(self, wiring: str):
        super().__init__()
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.right = wiring
        self.default = self.save()

    def reflect(self, signal):
        return self.forward(signal)
