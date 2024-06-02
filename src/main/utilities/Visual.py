import pygame


class Visual:
    def __init__(self, components: [object] = None, enigma: object = None):

        # get window height and width based on the screen size
        self.width = None
        self.height = None

        # set the margins and gap between components
        self.margins = {"top": 300, "bottom": 50, "left": 100, "right": 100}
        self.gap = 60

        # Machine
        self.enigma = enigma

        # set the text and path to be displayed
        self.input = ""
        self.output = ""
        self.path = None
        self.path_history = []
        self.last_keypress = None

        # set the components to be drawn
        self.components = components if components else []
        self.fonts = self.load_fonts()
        self.screen = self.init_window()

    @staticmethod
    def load_fonts():
        pygame.font.init()
        mono = pygame.font.SysFont("FreeMono", 25)
        bold = pygame.font.SysFont("FreeMono", 25, bold=True)
        return {"mono": mono, "bold": bold}

    def typing(self, key):
        if key.key == pygame.K_BACKSPACE:
            try:
                isSpace = self.input[-1] == " "
            except IndexError:
                isSpace = False
            self.input = self.input[:-1]
            self.output = self.output[:-1]
            if not isSpace:
                self.enigma.rotate_backward()
                if len(self.path_history) > 0:
                    if self.last_keypress == key:
                        self.path = self.path_history.pop()
                    else:
                        self.path_history.pop()
                        self.path = self.path_history.pop()
                else:
                    self.path = None

        elif key.key == pygame.K_RETURN:
            self.input = ""
            self.output = ""
            self.path = None
            self.enigma.reset()
        elif key.key == pygame.K_SPACE:
            self.input += " "
            self.output += " "
        elif key.unicode.isalpha():
            letter = key.unicode.upper()
            self.input += letter
            path, letter_encrypted = self.enigma.encrypt_signal(letter)
            self.output += letter_encrypted
            self.path = path
            self.path_history.append(path)
        self.last_keypress = key

    def init_window(self):
        self.width = 1600
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Enigma Machine Simulator")
        return self.screen

    def draw(self):
        self.screen.fill("#222831")

        # Draw the components

        x = self.margins["left"]
        y = self.margins["top"]
        w = (self.width - self.margins["left"] - self.margins["right"]
             - (len(self.components) - 1) * self.gap) / len(self.components)
        h = self.height - self.margins["top"] - self.margins["bottom"]
        for component in reversed(self.components):
            component.draw(self.screen, x, y, w, h, self.fonts["bold"])
            x += w + self.gap
        if self.path is not None:
            x = [self.width - self.margins["right"] - w / 2] # keyboard
            y = [self.margins["top"] + (signal + 1) * h / 27 for signal in self.path]
            for i in [4, 3, 2, 1, 0]:
                x.append(self.margins["left"] + i * (w + self.gap) + w * 3 / 4)
                x.append(self.margins["left"] + i * (w + self.gap) + w * 1 / 4)
            x.append(self.margins["left"] + w * 3 / 4)
            for i in [1,2,3,4]:
                x.append(self.margins["left"] + i * (w + self.gap) + w * 1 / 4)
                x.append(self.margins["left"] + i * (w + self.gap) + w * 3 / 4)
            x.append(self.width - self.margins["right"] - w / 2)

            for i in range(1, len(self.path)):
                if i < 10:
                    color = '#FF2E63'
                elif i < 12:
                    color = '#FDA638'
                else:
                    color = '#08D9D6'
                start = (x[i-1], y[i-1])
                end = (x[i], y[i])
                pygame.draw.line(self.screen, color, start, end, 5)

            # Draw the text
            text = self.fonts["bold"].render(self.input, True, "white")
            text_rect = text.get_rect(center=(self.width / 2, self.margins["top"] / 2))
            self.screen.blit(text, text_rect)

            output = self.fonts["mono"].render(self.output, True, "white")
            output_rect = output.get_rect(center=(self.width / 2, self.margins["top"] / 2 + 25))
            self.screen.blit(output, output_rect)

        names = ['Reflector', 'Rotor 1', 'Rotor 2', 'Rotor 3', 'Plugboard', 'Key/Lamp']
        y = self.margins["top"]*0.9
        for i, name in enumerate(names):
            text = self.fonts["bold"].render(name, True, "white")
            text_rect = text.get_rect(center=(self.margins["left"] + i * (w + self.gap) + w / 2, y))
            self.screen.blit(text, text_rect)


        pygame.display.flip()
        pygame.display.update()

    def start(self):
        run = True
        while run:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    else:
                        self.typing(event)
        pygame.quit()
