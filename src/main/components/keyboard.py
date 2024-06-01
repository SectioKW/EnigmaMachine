class Keyboard:

    @staticmethod
    def forward(letter: str):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter.upper())
        return signal

    @staticmethod
    def backward(signal: int):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
