#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

class ATM(): 
    serial_number = 0 
    
    def deposit(self, account, amount): 
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")
        
    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete")
        
    def check_currentbalance(self, account): 
        print(account.current_balance)
        
    def view_transactionsummary(self, account):
        print(f"Transaction Summary for {account.account_firstname} {account.account_lastname}:")
        print("New Balance:", account.current_balance)
        print("Transactions:")
        for transaction in account.transactions:
            print(transaction)
            
        with open("atm_transactions.txt", "a") as file:
            file.write(f"Transaction Summary for {account.account_firstname} {account.account_lastname}:\n")
            file.write(f"New Balance: {account.current_balance}\n")
            file.write("Transactions:\n")
            for transaction in account.transactions:
                file.write(transaction + "\n")
            file.write("\n")
        
class Accounts():
    def __init__(self, account_number, account_firstname, account_lastname, current_balance, 
                 address, email, serial_number):
        self.account_number = account_number 
        self.account_firstname = account_firstname
        self.account_lastname = account_lastname
        self.current_balance = current_balance
        self.address = address
        self.email = email
        self.serial_number = serial_number
        self.transactions = []
        
    
    def update_address(self, new_address): 
        self.address = new_address
        
    def update_email(self, new_email): 
        self.email = new_email    
        
    def update_serial_number(self, new_serial_number): 
        self.serial_number = new_serial_number
        
    def update_current_balance(self, new_current_balance): 
        self.current_balance = new_current_balance
 


        


# In[ ]:








# In[ ]:





