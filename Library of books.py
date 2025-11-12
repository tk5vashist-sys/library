print("Welcome")

def run():
    print("press 1 to continue")
    print("press 2 to exit")

    a = int(input("press number for continue and exit"))
    if a==1:
       book()
    elif a==2:
         print("thanks for visit")

def book():

 print("press 1 for book:1")
 print("press 1 for book1")
 print("press 1 for book1")
 print("press 1 for book1")
 
 b=int(input("Enter book number to continue"))
 if b==1:
    print("MAHABHARAT- The Mahabharata is an ancient Sanskrit epic that narrates the Kurukshetra War, a conflict between two sets of cousins, the Pandavas and Kauravas, for control of the kingdom of Hastinapura")

    run()

 elif b==2:
    print("RAMAYAN - The Ramayana is an ancient Indian epic about the life of Lord Rama, detailing his exile, the abduction of his wife Sita by the demon king Ravana, the war to rescue her, and his eventual return to the throne of Ayodhya")

    run()

 elif b==3:
    print("JAI SHREE RAM")

    run()
book()
