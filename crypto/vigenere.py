import string
def alphabet_position(letter):
        base = ord('a')
        return ord(letter.lower()) - base
        
def rotate_charactor(char, rot):
        base = ord('a')
        if char.isalpha():
                codedLNum = (alphabet_position(char) + rot) % 26
                codedL = chr(codedLNum + base)
                if char.upper() == char:#char equals uppercase char make sure it returns uppercase
                        return codedL.upper()
                elif char.lower() == char:#char equals lowercase char make sure it returns lowercase
                        return codedL.lower()
                """
                else:
                        print('Oops!')
                """
        elif not(char.isalpha()):
                return char

def encrypt(stuffHere, vig):
    #New(encryption should ignore spaces
    encrypted_message = ''
    key_pos = 0
    for j in range(len(stuffHere)):
        
        encrypted_message += rotate_charactor(stuffHere[j],alphabet_position(vig[key_pos]))

        if stuffHere[j].isalpha():
            key_pos = (key_pos + 1) % len(vig)

    return encrypted_message
        




    #Old (encryption string written before accounting for spaces
    """
    encrypted_message = ''
    #need a way to link vig position and string position
    vig_string = ''
    key_length = len(vig)
    strng_length = len(stuffHere)
    #Create long key-based parallel string to referance
    for i in range(strng_length // key_length + 1): #will have extra but better than rounding below and not having enough
        vig_string += vig
    #print(vig_string) #TEST
    #
    for j in range(strng_length):
        
        encrypted_message += rotate_charactor(stuffHere[j],alphabet_position(vig_string[j]))
    return encrypted_message
    """
    
def header():
    """
    print('x' * 10, 'vigenere', 'x' *10)
    print('-' * 28)
    print(' ' * 28)
    """
    a=1

#Implied main  
"""
header()
user = input('What would you like to encrypt?')
not_valid = True
while not_valid: 
    user2 = input('What is your super-secret password?')
    if 0 == 0: #TODO test for valid
        not_valid = False

print(encrypt(user,user2))
"""
