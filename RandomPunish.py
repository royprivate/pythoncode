import random


def Help():
    print("""
    Creator: Roy de Jong
    Welcome to the random punisher!
    Type: "Add" to add a new punishment to the list
    Type: "list" to check the current list of punishments
    Type: "Roll" to roll the punishments
    """)
def write_list(lst):
    for item in lst:
        print(" - " + str(item))


punishment = []
Help()
while True:
    b = raw_input('> ')

    if b == "add":
        q = raw_input('Add a punishment: ')
        print('Added the punishment to the list, to see the list type "list"')
        punishment.append(q)

    elif b == int:
        print('Ints are not allowed!')

    #All commands that can be executed
    elif b == "list":
        write_list(punishment)
        

    elif b == "roll":
        if len(punishment) < 2:
            print('You have to add atleast 3 punishments')
        else:
             print('We are rolling the punishment!')
             print('Omg hold tight!!!!!!')
             print("The punishment is: " + '"' + random.choice(punishment) + '"')
        
    #Closing   
    elif b == "close":
        break
    #Closing
    elif b == "clear":
        break
    #Closing
    elif b == "stop":
        break
        continue

    
           



