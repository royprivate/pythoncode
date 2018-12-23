#ECO-CALC
# Zundag december 23
#Last edited: 11:43
# @Author R. de Jong
import os



#Options 
def Options():
    print("""
     Welcome to ECO-CALC. 
     You can use this program to calculate taxes. 
     Or calculate your networth etc.

    

     Commands: 
     1 - Omzet 
         (Type Omzet to calculate the omzet. )
     2 - Bruto
         (Type bruto calculate the bruto. )
     3 - Netto
         (Type netto to calculate the netto. )
     4 - Help
         (Type help to see this help menu. )
    """)

Options()

#Bruto calculation
def bruto (omzet, inkoop):
    print(omzet - inkoop)

#Omzet calculation
def omzet (afzet, verkoop):
    print(afzet * verkoop)
    
#Nettowinst calculation
def netto(bruto, kosten):
    print(bruto - kosten)



#While true
while True:
    #Looping constant to this 
    const = raw_input("> ")
    if const == "omzet":
        afzet = int(raw_input("Afzet > "))
        verkoop = int(raw_input("Verkoop > "))
        omzet(afzet, verkoop)
    
    elif const == "help":
        Options()

    elif const == "bruto":
        omzet = int(raw_input('Omzet > '))
        inkoop = int(raw_input('Inkoop prijs > '))
        bruto(omzet, inkoop)


    #Asking the user to input the values 
    #And Returning the function netto
    elif const == "netto":
        bruto = int(raw_input('Bruto winst > '))
        kosten = int(raw_input('Bedrijfs kosten > '))
        netto(bruto, kosten)
        continue

    elif const == "clear":
        os.system('clear') 
    elif const == "stop":
        break
    



