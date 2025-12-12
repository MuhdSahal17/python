import calculator as calc

while True:
    print("--CALCULATOR--")
    print("1.Add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.Quit")

    choice = int(input("Enter Your Choice:"))

    if choice == 5:
        print("Exited")
        break
    else:
        a = int(input("Enter First Number:"))
        b = int(input("Enter Second Number:"))
        
        if choice == 1:
            print(calc.add(a,b))
        elif choice == 2:
            print(calc.sub(a,b))
        elif choice == 3:
            print(calc.mul(a,b))
        elif choice == 4:
            print(calc.div(a,b))    
        else:
            print("Invalid")