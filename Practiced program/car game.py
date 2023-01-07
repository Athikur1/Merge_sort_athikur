def cg ():
    st = 0
    while True:
        x = input(".>").lower()
        if x == 'help':
            print('START to Start\nSTOP to stop\nQ to quit game')
        elif x == 'start' and st == 1:
            print("The car is already started")
        elif x == 'start':
            print("The car is started")
            st =1
        elif x == 'stop' and st !=1:
            print('The car is already stoped')
        elif x == 'stop':
            print('The car is stoped')
            st = 0
        elif x == 'q':
            print("Game Exit")
            break
        else:
            print("i don't uderstand")


