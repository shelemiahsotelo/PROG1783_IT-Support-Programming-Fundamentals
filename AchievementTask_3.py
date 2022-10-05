#8223190 - Shelemiah Sotelo
#Task 3 
#Input Length Checker


invalid = True

hasUpper = 0
hasNumber = 0

while invalid:
    
    print("Please enter username:")
    name = input().strip()

    if len(name) == 1:
        print("Sorry, username must be longer than one letter.")
        
        
    elif len(name) > 20:
        print("Sorry, username cannot be more than 20 letters in length.")

        
        
    else:
        for aCharacter in name:
            if aCharacter.isupper():
                hasUpper += 1

            if aCharacter in "0123456789":
                hasNumber += 1
        
        if hasUpper >= 1 and hasNumber >= 1:
            print("Thanks!")
            invalid = False
        elif hasUpper == 0:
            print("Username must have Uppercase alphabet.")
        elif hasNumber == 0:
            print("Username must have number/s (0-9)")