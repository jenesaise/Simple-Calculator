#1.	Create a basic calculator that can perform addition, subtraction, multiplication, and division. This will help you understand functions and user input.
 
Num1 = int(input("Enter A Number = "))
Num2 = int(input("Enter Another Number = "))
def Menu():
    ReqChoice = 1,2,3,4
    Play = True
    global Num1, Num2
    while Play == True:
        Choice = 5
        while Choice == 5:
            print("1 = Addition")
            print("2 = Subtraction")
            print("3 = Multiplication")
            print("4 = Division")
            Choice = int(input("Enter Your Choice = "))
        while Choice not in ReqChoice:
            Choice = int(input("Re-enter Your Choice = "))
               
        if Choice == 1:
            print(Num1 + Num2)
        elif Choice == 2:
            print(Num1 - Num2)
        elif Choice == 3:
            print(Num1 * Num2)
        elif Choice == 4:
            print(Num1 / Num2)
            
        Again = input("Would You Like To Continue Using The Calculator? (y/n) = ").lower()
        if Again == "n":
            Play = False

    print("Thanks For Using The Calculator!")
Menu()