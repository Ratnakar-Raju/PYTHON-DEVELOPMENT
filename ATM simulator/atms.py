import time

print("Please insert Your CARD")

time.sleep(5)

password=1234

pin=int(input("enter your atm pin "))

balance=5000

if pin==password:
    while True:
    
            print("""
        1 == balance
        2 == withdraw balance
        3 == deposit balance
        4 == exit
        """
                  )
            try:
                option=int(input("Please enter your choise "))
            except:
                print("Please enter valid option")

            if option==1:
                print(f"Your current balance is {balance}")

                print("____________________________________________")
                
                print("____________________________________________")


                print("____________________________________________")


            if option==2:

                withdraw_amount=int(input("please enter withdraw_amount "))
                
                print("_____________________________________________")


                print("____________________________________________")

                print("____________________________________________")


                balance=balance-withdraw_amount
                
                print("____________________________________________")

                print("____________________________________________")


                print(f"{withdraw_amount} is debited from your account")
                
                print("____________________________________________")

                print("____________________________________________")


                print(f"your updated balance is {balance}")
                
                print("____________________________________________")

                print("____________________________________________")


            if option==3:

                deposite_amount=int(input("please enter deposite_amount"))
                
                print("____________________________________________")

                

                print("____________________________________________")


                balance=balance+deposite_amount
                
                print("____________________________________________")

                print("____________________________________________")


                print(f"{deposite_amount} is credited to your account")
                
                print("____________________________________________")

                print("____________________________________________")


                print(f"your updated balance is {balance}")
                
                print("____________________________________________")

                print("____________________________________________")


            if option==4:
                break

                





   
else:
    print("wrong pin please try again")
