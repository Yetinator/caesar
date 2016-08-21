from helpers import alphabet_position, rotate_character, user_input_is_valid
from sys import argv, exit

def encrypt(stuffHere, rot = 13):
    encrypted_message = ''
    for i in stuffHere:
        encrypted_message += rotate_character(i,rot)
    return encrypted_message
        
"""
#Implied Main
#not_valid = True
if user_input_is_valid(argv):
    user = input('What would you like to encrypt?')
    rota = int(argv[1])
    print(encrypt(user,rota))
print("The program didn't exit in the test function")  
"""   
   
   

