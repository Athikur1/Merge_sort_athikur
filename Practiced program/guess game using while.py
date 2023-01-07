secret_number = 7

no_guess_made = 1

while no_guess_made <=3:
    n = int(input('Guess : '))
    if(n == secret_number):
        print('win')
        break
    no_guess_made = no_guess_made + 1
else: 
    print("u u r fail")
    


