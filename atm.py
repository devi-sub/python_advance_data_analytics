amount=10000
pin= int(input("enter the pin:"))
while True:
    print("MENU: 1.withdraw 2. enquiry")
    choice=int(input("enter your choice:"))
    if choice==1:
        withdraw_amount=int(input("enter the withdraw amount:"))
        if withdraw_amount<=amount:
            amount=amount-withdraw_amount
            print("remaining balance:",amount)
        else:
            print("insufficient balance")

    elif choice==2:
            print(" balance amount:",amount)

    else:
            print("invalid choice")
            break
