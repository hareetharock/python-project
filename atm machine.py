import time

print("Please insert your card")
 
time.sleep(5)
password=1234

pin=int(input("Enter your ATM pin --> "))
balance=10000

if pin==password:
    while True:
    
        print("please select and option  ")
        
        print("===========================================================================")
        print(""" 
                1 == Balance inquiry                              2 == Cash withdrawal
                3 == cash deposit                                 4 == Exit""")
        
        try:
            option=int(input("please Enter your choice  "))
            print("===========================================================================")
        except:
            print("Please choose valid option")
            print("===========================================================================")
        if option == 1:
            print(f"Your currant Balance is {balance}")
        if option == 2:
            withdraw_amount=int(input("Please Enter withdrawal Amount  "))
            balance=balance-withdraw_amount
            print("===========================================================================")
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your Updated balance is {balance}")
        if option == 3:
            cash_deposit=int(input("Please enter deposit amount  "))
            balance=balance+cash_deposit
            print("===========================================================================")
            print(f"{cash_deposit} amount is deposited in your account")
            print(f"Your Updated balance is {balance}")
            print("===========================================================================")
        if option == 4:
            break
else:
    print("wrong pin please try again")