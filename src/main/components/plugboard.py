from typing import List
from src.main.components.component import Component
import pygame


class Plugboard(Component):
    def __init__(self, pairs: dict):
        super().__init__()
        self.right = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for k, v in pairs.items():
            self.right = self.right[:self.right.find(k)] + v + self.right[self.right.find(k) + 1:]
            self.right = self.right[:self.left.find(v)] + k + self.right[self.left.find(v) + 1:]
        self.default = self.save()

    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int, font: pygame.font.Font):
        r = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), r, 2, 15)

        for i in range(26):
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width / 4, y + (i + 1) * height / 27))
            screen.blit(letter, text_rect)

            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width * 3 / 4, y + (i + 1) * height / 27))
            screen.blit(letter, text_rect)
