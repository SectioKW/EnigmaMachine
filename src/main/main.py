from src.main.feature.enigma import Enigma


if __name__ == '__main__':
    enigma = Enigma()
    while True:
        letter = input('Enter a letter: ')
        if letter == 'exit':
            break
        print(enigma.encrypt_message(letter))
