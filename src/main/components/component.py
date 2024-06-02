from typing import List
import pygame

class Component:
    def __init__(self):
        self.right = None
        self.left = None
        self.default = self.save()

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def load(self):
        self.right, self.left = self.default

    def save(self):
        return self.right, self.left

    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int, font: pygame.font.Font):
        r = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), r, 2, 15)

        for i in range(26):
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width / 4, y + (i + 1) * height / 27))
            screen.blit(letter, text_rect)

            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width * 3 / 4, y + (i + 1) * height / 27))
            screen.blit(letter, text_rect)