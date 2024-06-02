from src.main.feature.enigma import Enigma


if __name__ == '__main__':
    enigma = Enigma()
    while True:
        message = input('Enter message : ')
        if message == 'exit':
            break
        enigma.encrypt_message(message)
