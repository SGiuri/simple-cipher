from random import randint


class Cipher:
    def __init__(self, key=None):
        if key == None:
            key = self.generate_Key(101)

        self.key = key.lower()
        print(self.key)
        self.shift_key = [ord(key_char) - ord("a") for key_char in key]

    def encode(self, text):
        encoded = ""
        j = 0
        for letter in text:
            shift = ord(letter) + self.shift_key[j % len(self.shift_key)]
            if shift > ord("z"):
                shift = shift - (ord("z") - ord("a") + 1)
            encoded_letter = chr(shift)
            encoded += encoded_letter
            j += 1
        return encoded

    def decode(self, text):
        decoded = ""
        j = 0
        for letter in text:
            shift = ord(letter) - self.shift_key[j % len(self.shift_key)]
            if shift < ord("a"):
                shift = shift + (ord("z") - ord("a") + 1)
            decoded_letter = chr(shift)
            decoded += decoded_letter
            j += 1
        return decoded

    def generate_Key(self, lenght):
        new_key = ""
        for l in range(lenght):
            new_key += chr(randint(ord("a"), ord("z")))
        return new_key