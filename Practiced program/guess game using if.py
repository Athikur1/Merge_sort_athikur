secret_number = 7

i = 1
def g():
    if i <=3:
        n = int(input("Guess 1 : "))
        if n == secret_number:
            print("Your have won")
        elif n != secret_number:
            n1 = int(input("Guess 2: Try again..!  "))
            if n1 == secret_number:
                print("Your have won")
            elif n1 != secret_number:
                n2 = int(input("Guess 3: Try again..!  "))
                if n2 == secret_number:
                    print('Your have won')
                else:
                    print("Fail come back tommorow.")    
    
        
        
        
        
