import random
import sys
import time

class Account:
    def __init__(self,balance,acc_no,pin):
        self.balance=balance
        self.acc_no=acc_no
        self.pin=pin
    def credit(self, amount):
     if amount > 0:
        while True:
            password = input("Enter your 4 digit password to credit the amount to your bank account : ")
            if password == self.pin:
                self.balance += amount
                print(f"The amount is credited {amount} to the account number {self.acc_no}")
                break
            else:
                print("Incorrect password............\nTry again")
                reset = input("Do you want to reset the password (y/n) : ").lower()
                if reset == 'y':
                    ph = input("Enter your phone number : ")
                    print("The OTP has been sent to your phone number ")
                    otp_store = self.otp()
                    self.otp_check(otp_store)
                    break
                else:
                    print("Please try entering the password again.")
     else:
        print("Invalid credit")
           
    def debit(self, amount):
     if amount > 0 and amount <= self.balance:
        while True:
            password = input("Enter the password : ")
            if self.pin == password:
                for i in range(1,101):
                    sys.stdout.write(f"\r Debiting {i}%")
                    sys.stdout.flush()
                    time.sleep(0.05)
                self.balance -= amount
                print(f"The amount is debited {amount} from the bank account {self.acc_no}")
                break
            else:
                print("Incorrect password............\nTry again")
                reset = input("Do you want to reset the password (y/n) : ").lower()
                if reset == 'y':
                    ph = input("Enter your phone number : ")
                    print("The OTP has been sent to your phone number ")
                    otp_store = self.otp()
                    self.otp_check(otp_store)
                    break
                else:
                    print("Please try entering the password again.")
     else:
        print("Insufficient funds........")

    
    def otp(self):
        otp=random.randint(1000,9999)
        print(f"Your otp is {otp}")
        return otp
        
    def otp_check(self,otp):
        enter=int(input("Enter your OTP : "))
        if enter==otp:
            print("Your entered otp is correct .............")
            new_pass=input("Enter the new password : ")
            self.pin=new_pass
            print(f"New password {new_pass} is created successfully ")
        else:
            print("Entered OTP is wrong .....................\nTry again")
    def check_balance(self):
        while True:
           password=(input("Enter the password to check the balnace............"))
           if(self.pin==password):
               for i in range(1,101):
                   sys.stdout.write(f"\rchecking balance {i}%")
                   sys.stdout.flush()
                   time.sleep(0.05)
               print("Done successfully.")
               print(f"The balance is {self.balance} \nand the account number is {self.acc_no}")
               break
           else:
            print("Invalid passoword")
    
    def reset(self):
        otp_store = self.otp()
        if self.otp_check(otp_store):
            new_pass = input("Enter the new password : ")
            self.pin = new_pass
            print(f"New password {new_pass} is created successfully ")
        else:
            print("Failed to reset password due to invalid OTP.")
      
    def ministatement(self):
        print("||** MiniStatement **||")
        print(f"You have {self.balance} ")
        print(f"Your account number is {self.acc_no}")
        print("ThankYou visit Again...........")
        
    def online_transaction(self):
        confirm=input("Do you want to do online transaction : ").lower()
        if(confirm=='y'):
            acno=input("Enter the account number : ")
            length=len(acno)
            if(length < 11):
                print("Invalid account number")
                print("Account number should be in 11 digits")
                print("Try again from starting.....................................")
                
            else:
                transaction=int(input("Enter the amount : "))
                acc.balance-=transaction
                print(f"{transaction} rupees have been transacted to the {acno} succesfully")
                
                print("****************************************")
                print(f"Now you left with {acc.balance} rupees after online transaction")
                
        else:
            print("Invalid choice")
            
            
            
    
def menu():
    print("|| Bank Menu || : ")
    print("1.Credit")
    print("2.Debit")
    print("3.check balance")
    print("4.Reset your password")
    print("5.MiniStatement")
    print("6.Online transaction")
    print("7.Exit")
    
    choice=(input("Enter your choice now (1-6) : " ))
    
    
    return choice


acc = Account(balance=10000, acc_no="12345678", pin="2784")



while True:
    
    
    option = menu()
    
    if option == '1':
        amt = float(input("Enter amount to credit: "))
        acc.credit(amt)
    
    elif option == '2':
        amt = float(input("Enter amount to debit: "))
        acc.debit(amt)
    
    elif option == '3':
        acc.check_balance()
    
    elif option == '4':
        acc.reset()
    
    elif option == '5':
        acc.ministatement()
        break
    
    
    elif option=='6':
        acc.online_transaction()
        
    
    elif option=='7':
        print("Thank you visit again")
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        