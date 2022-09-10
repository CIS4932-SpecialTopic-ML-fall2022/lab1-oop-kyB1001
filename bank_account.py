
import math as math
import numpy as np
import sys
import time

class BankAccount:
        
    # Create a constructor with parameters: accountNumber, name, balance. (20 pts)     
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    #  Create a Deposit() method which manages the deposit actions. (10 pts) 
    
    def Deposit(self):
        cont = int(input("Enter 1: Deposit Money\nEnter 2: Cancel\n"))
        
        if cont == 1:
            deposit = input("Enter the Deposit amount:  ")
            deposit = float(deposit)
            self.balance = self.balance + deposit
            print("Your deoposit has been made!\nYour account balance is {:.2f} ".format(self.balance))

        elif cont == 2:
                print("Thank you for choosing to bank with Royalty Banking!") 
  
        else:
            print("Invalid Input")  
                        
            
    
    # Create a Withdrawal() method  which manages withdrawals actions. (10 pts) 
    def Widthdrawl(self):
        cont = int(input("Enter 1: Withdrawal Money\nEnter 2: Cancel\n"))
        
        if cont == 1:
            while True:
                withdrawal = input("Enter the Withdrawal amount:  ")
                withdrawal = float(withdrawal)
                
                if(withdrawal > self.balance):
                    print("Insufficient Funds\n Available account balance {:.2f}\n".format(self.balance))
                else:
                    self.balance = self.balance - withdrawal
                    print("Your widthdrawl has been succesfully made!\nYour account balance is {:.2f}\n".format(self.balance))
                    break

        elif cont == 2:
                print("Thank you for choosing to bank with Royalty Banking!") 
  
        else:
            print("Invalid Input")  
                   
    # Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account. (10 pts) 
    def bankFees(self):
        fees = self.balance * .05 
        print("Your current Bank Fee is: {:.2f}\n".format(fees))
    
    # Create a display() method to display account details. (10 pts)    
    def Display(self):
        print("Account Information:\n")
        print(" Account Number: {}\n Account Owener: {}\n Account Balance:5 {}\n".format(self.accountNumber,self.name,self.balance))
    
if __name__ == "__main__":
   
    accountInfo = BankAccount(1235432,"RaCaria Burgess",10000000)
    
    print("Hello {}...\n".format(accountInfo.name))
    time.sleep(1)
    print("Firstly, Royalty Banking hopes that all is well...\n")  
    time.sleep(1)
    print("To protect your identitiy\n")  
    time.sleep(1)    
    verification = int(input("Please Confirm your Account Numer:  "))
   
    select = 0
    if(accountInfo.accountNumber == verification):
            
        while True: 
            select = input("Please select from the following options:\n Enter 1: To Make a Deposit\n Enter 2: To Make a Widthdrawl\n Enter 3: To View Bankfees\n Enter 4: To View Account Details\n Enter 5: To Exit\n")
            select = int(select)
            
            if select == 1: #Enter 1: To Make a Deposit  
                accountInfo.Deposit()
            
            elif select == 2: # Enter 2: To Make a Widthdrawl
                accountInfo.Widthdrawl()
                
            elif select == 3: # Enter 3: To View Bankfees
                accountInfo.bankFees()
                
            elif select == 4: # Enter 4: To View Account Details
                accountInfo.Display()

            elif select == 5: # Enter 5: To Exit              
                break
            
            else:
                print("Invalid Entry\n")
        
        print("Thank you for choosing to bank with Royalty Banking!\n")  
         
    else:
      print("Sorry, we cannot validate your account number. Have a Beautiful Day!\n")  
      
