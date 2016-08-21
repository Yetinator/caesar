def get_initials(fullname = None):
    """ 
    Given a person's name, return the person's initials (uppercase) 
    """
    if fullname == None:
        fullname = input('What is your name?')
        prnt = True
    words = fullname.split()
    initialsString = ''
    for i in words:
        initialsString += i[0].capitalize()

    return initialsString

#Implied Main
"""    
get_initials()
"""

