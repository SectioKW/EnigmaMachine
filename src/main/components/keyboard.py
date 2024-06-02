import pygame


class Keyboard:

    @staticmethod
    def forward(letter: str):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter.upper())
        return signal

    @staticmethod
    def backward(signal: int):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter

    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int, font: pygame.font.Font):
        r = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), r, 2, 15)

        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, "grey")
            text_rect = letter.get_rect(center=(x + width / 2, y + (i + 1) * height / 27))
            screen.blit(letter, text_rect)
