def alphabet_position(letter):
        base = ord('a')
        return ord(letter.lower()) - base
        
def rotate_character(char, rot):
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
                
def user_input_is_valid(cl_args):
    if len(cl_args) == 2: # Test for number of argv
        #TODO test for num
        if cl_args[1].isdigit():
            return True
    #print('Usage: python3 ceasar.py n')
    exit()
    #return False
