first=float(input("enter first number:"))
second=float(input("enter second number:"))
choice=0
while choice<5:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("enter your choice"))
    if choice==1:
        c=first+second
        print("sum is:",c)
    elif choice==2:
        c=first-second
        print("difference is:",c)
    elif choice==3:
        c=first*second
        print("multiplication is:",c)
    elif choice==4:
        c=first/second
        print("division is:",c)
    elif choice==5:
        break
    else :
        print("invalid")
     
    
