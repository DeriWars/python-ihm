from random import Random

class Encryption():    
    def encrypt(self, text, key):
        random = Random(key)
        encrypted_text = ""
        
        for char in text:
            value = random.randint(10, 26)
            encrypted_text += chr(ord(char) + value) if ord(char) + value < 256 else char
            
        return encrypted_text

    def decrypt(self, text, key):
        random = Random(key)
        decrypted_text = ""
        
        for char in text:
            value = random.randint(10, 26)
            decrypted_text += chr(ord(char) + value) if ord(char) + 2 * value >= 256 else chr(ord(char) - value)
            
        return decrypted_text