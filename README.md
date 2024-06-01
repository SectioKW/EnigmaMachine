# Enigma Machine
Python approach to implement the Enigma Machine.
structure:
- `enigma.py`: The main implementation of the Enigma Machine.
- `rotors.py`: The implementation of the rotors used in the Enigma Machine.
- `plugboard.py`: The implementation of the plugboard used in the Enigma Machine.
- `keyboard.py`: The implementation of the keyboard used in the Enigma Machine.
- `reflector.py`: The implementation of the reflector used in the Enigma Machine.
- `KeyReader.py`: KeyReader class to read the key from keySetting.json
- `keySetting.json`: The key setting file for the Enigma Machine.

Key Setting:
- `plugboard`: The plugboard setting for the Enigma Machine. (e.g. {"A": "B", "C": "D"})
- `rotors`: The rotors used in the Enigma Machine. 
- `rotorOrder`: The order of the rotors used in the Enigma Machine. (e.g. [I, II, III])
- `initialPosition`: The initial position of the rotors used in the Enigma Machine. (e.g. [A, A, A] which translates to [1, 1, 1])
- `reflector`: The reflector used in the Enigma Machine. (e.g. "B")

Enigma Machine Sequence:
1. Keyboard input
2. Plugboard (Change the input based on the plugboard setting)
3. Rotors (Rotate the rotors based on the initial position and ring setting, then change the input based on the rotor setting)
4. Reflector (Reflect the input based on the reflector setting)
5. Rotors Backward (Rotate the rotors back based on the initial position and ring setting, then change the input based on the rotor setting)
6. Plugboard Backward (Change the input back based on the plugboard setting)
7. Output


## Installation
Make a venv and install the requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Usage
To run the Enigma Machine, run the following command:
```python main.py```

To change the key setting, modify the `keySetting.json` file.

This is the default key setting based on the Enigma Machine I:
```
{
  "plugboard" : {
    "A" : "R",
    "G" : "K",
    "O" : "X"
  },
  "rotors" : {
    "I" : {
      "wiring" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
      "notch" : "Q"
    },
    "II" : {
      "wiring" : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
      "notch" : "E"
    },
    "III" : {
      "wiring" : "BDFHJLCPRTXVZNYEIWGAKMUSQO",
      "notch" : "V"
    },
    "IV" : {
      "wiring" : "ESOVPZJAYQUIRHXLNFTGKDCMWB",
      "notch" : "J"
    },
    "V" : {
      "wiring" : "VZBRGITYUPSDNHLXAWMJQOFECK",
      "notch" : "Z"
    }
  },
  "reflectors" : {
    "A" : "EJMZALYXVBWFCRQUONTSPIKHGD",
    "B" : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C" : "FVPJIAOYEDRZXWGCTKUQSBNMHL"
  },
  "reflector" : "A",
  "rotorOrder" : ["I", "II", "III"],
  "ringSettings" : ["A","A","A"],
  "initialPositions" : ["A", "A", "A"]
}
```