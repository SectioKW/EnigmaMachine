from src.main.components.component import Component


class Rotor(Component):
    def __init__(self, wiring: str, notch: str = 'A'):
        super().__init__()
        self.right = wiring
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.notch = notch

    def rotate(self, n: int = 1, forward: bool = True):
        for _ in range(n):
            if forward:
                self.right = self.right[1:] + self.right[0]
                self.left = self.left[1:] + self.left[0]
            else:
                self.right = self.right[-1] + self.right[:-1]
                self.left = self.left[-1] + self.left[:-1]

    def set_ring(self, n: str):
        n = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(n.upper())
        self.rotate(n, False)
        n_notch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(self.notch)
        self.notch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(n_notch-n) % 26]

    def rotate_to_letter(self, letter: str):
        n = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(letter.upper())
        self.rotate(n)

    def display(self):
        print(f'Right : {self.right}')
        print(f'Left : {self.left}')
        print()

