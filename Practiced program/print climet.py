

def to_check_climet():
    temp = int(input('Enter Temperature: '))
    temp_measure = input('Entred temp is in Fharenheit(F) or Celcious(C): ')
    if temp_measure.upper() == 'F':
    
        return(float(temp-32)*0.5556)
    else:
        return(temp)
    
f = to_check_climet()

def result():
    if float(f) <=22:
        print("its cold dude ")
    elif 22 < float(f) <29:
        print('Its normal')
    else:
        print("its hot")


print(result())

