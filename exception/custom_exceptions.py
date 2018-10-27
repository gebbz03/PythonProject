class VowelNotAccepted(Exception):
    def __init__(self,message,status):
        self.message=message
        self.status=status

def check_chars(word):
    for char in word:
        if char.lower() in ['a','e','i','o','u']:
            raise VowelNotAccepted('Vowel is not accepted',101)
    return word

try: 
    print(check_chars("love"))
except Exception as e:
    print("Error reason: ",e.message)