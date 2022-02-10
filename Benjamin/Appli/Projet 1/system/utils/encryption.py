from random import Random

class Encryption():
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, text):
        random = Random(self.key)
        encrypted_text = ""
        
        for char in text:
            value = random.randint(10, 26)
            encrypted_text += chr(ord(char) + value) if ord(char) + value < 256 else char
            
        return encrypted_text

    def decrypt(self, text):
        random = Random(self.key)
        decrypted_text = ""
        
        for char in text:
            value = random.randint(10, 26)
            decrypted_text += chr(ord(char) + value) if ord(char) + 2 * value >= 256 else chr(ord(char) - value)
            
        return decrypted_text