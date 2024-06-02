from src.main.components.component import Component
import pygame

class Rotor(Component):
    def __init__(self, wiring: str, notch: str = 'A'):
        super().__init__()
        self.right = wiring
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.notch = notch
        self.default = self.save()

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

    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int, font: pygame.font.Font):
        r = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), r, 2, 15)

        for i in range(26):
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width / 4, y + (i + 1) * height / 27))
            if i == 0:

                letter = font.render(self.left[i], True, (43, 43, 43))
                pygame.draw.rect(screen, (109, 183, 227), text_rect, border_radius=5)
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, (35, 171, 252))
            if i == 0 and self.left[i] == self.notch:
                letter = font.render(self.left[i], True, (245, 245, 245))
                pygame.draw.rect(screen, (85, 107, 230), text_rect, border_radius=5)
            screen.blit(letter, text_rect)

            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width * 3 / 4, y + (i + 1) * height / 27))
            screen.blit(letter, text_rect)
