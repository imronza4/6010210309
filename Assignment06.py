import random
import string

def randomString(stringLength):
"""Generate a random string of fixed length """
    letters = string.ascii_lowercase
    for i in range(stringLength)):
        return ''.join(random.choice(letters) 

if __name__ = '__main__':
   charlist = randomString(10)
   print(charlist)
