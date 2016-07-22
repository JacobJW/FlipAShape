
def flip_it ():

    initial = True
    run = False
    while initial == True:
        
        base = input("How many units do you want the base to be? \n")
        print("\n")
        try:   
            if base.isdigit() == False or int(base) < 2: 
                print("Sorry, that's not a valid input. Please use only numbers and make the base larger than 1. \n")
            break
        except ValueError:
            print("Sorry, that's not a valid input. Please use only numbers and make the base larger than 1. \n")
                
        if base.isdigit() == True and int(base) >= 2:
            initial = False
            
    run = True
        
    if run == True:
       
        # Converts base into an int for usage later on in multiplication
        base = int(base)
                
        Triangle = []
        
        # Creates the base of #'s and makes each row have 1 less # , plus indents it by one space to keep triangle format
        
        for num in range(base, 0, -1):
            Triangle.insert(0, [' #' * num])
            Triangle[0].insert(0, ' ' * (base - num))

        # Joins the separate strings of spaces and #'s together 
        for num in range(0, base):
            Triangle[num] = ''.join(Triangle[num])
                    
        for row in Triangle:
            print(row)
        
        print(" \nFLIPPING . . . \n")

        # Since each row is its own list, to flip we print the rows in reverse.
        
        for num in range(base -1, -1, -1):
            print(Triangle[num])
            
flip_it()
