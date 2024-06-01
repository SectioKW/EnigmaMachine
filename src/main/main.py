from src.main.components.component import *

def main():
    pass
    # # I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 16)
    # # II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 4)
    # # III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 21)
    # # IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 9)
    # # V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 25)
    # # A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
    # # B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    # # C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')
    # # PB = Plugboard(['AR', 'GK', 'OX'])
    # # KB = Keyboard()
    # # rotors = [III,II,I]
    # # reflector = A
    #
    # signal = KB.forward('A')
    # signal = PB.forward(signal)
    # for rotor in rotors:
    #     signal = rotor.forward(signal)
    # signal = reflector.reflect(signal)
    # for rotor in reversed(rotors):
    #     signal = rotor.backward(signal)
    # signal = PB.backward(signal)
    # letter = KB.backward(signal)
    # print(letter)

if __name__ == '__main__':
    main()


