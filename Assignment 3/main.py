#!/usr/bin/env python
# coding: utf-8

# In[7]:


import Accounts

Account1 = Accounts.Accounts()

print("Account 1")
Account1.account_firstname = "Ivan"
Account1.account_lastname = "Villena"
Account1.current_balance = 1000
Account1.address = "Santolan Pasig"
Account1.email = "villenaic@gmail.com"

print(Account1.account_firstname)
print(Account1.account_lastname) 
print(Account1.current_balance) 
print(Account1.address) 
print(Account1.email)

print()

Account2 = Accounts.Accounts()
Account2.account_firstname = "John"
Account2.account_lastname = "Doe"
Account2.current_balance = 2000
Account2.address = "Gold Street Quezon City"
Account2.email = "johndoe@yahoo.com"

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname) 
print(Account2.current_balance) 
print(Account2.address) 
print(Account2.email)


# In[10]:


import Accounts
import ATM

Account1 = Accounts.Accounts()

print("Account 1")
Account1.account_firstname = "Ivan"
Account1.account_lastname = "Villena"
Account1.current_balance = 1000
Account1.address = "Santolan Pasig"
Account1.email = "villenaic@gmail.com"

print(Account1.account_firstname)
print(Account1.account_lastname) 
print(Account1.current_balance) 
print(Account1.address) 
print(Account1.email)

print()

Account2 = Accounts.Accounts()
Account2.account_firstname = "John"
Account2.account_lastname = "Doe"
Account2.current_balance = 2000
Account2.address = "Gold Street Quezon City"
Account2.email = "johndoe@yahoo.com"

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname) 
print(Account2.current_balance) 
print(Account2.address) 
print(Account2.email)

ATM1 = ATM.ATM()
ATM1.deposit(Account1, 500)
ATM1.check_currentbalance(Account1)

ATM1.deposit(Account2, 300)
ATM1.check_currentbalance(Account2)


# In[8]:


import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=123456, account_firstname="Ivan", account_lastname="Villena", current_balance=1000,
                            address="Santolan Pasig", email="villenaic@gmail.com")


print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname) 
print(Account1.current_balance) 
print(Account1.address) 
print(Account1.email)

print()

Account2 = Accounts.Accounts(account_number=654321, account_firstname="John", account_lastname="Doe", current_balance=2000,
                            address="Gold Street Quezon City", email="johndoe@yahoo.com")

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname) 
print(Account2.current_balance) 
print(Account2.address) 
print(Account2.email)

ATM1 = ATM.ATM()
ATM1.deposit(Account1, 500)
ATM1.check_currentbalance(Account1)

ATM1.deposit(Account2, 300)
ATM1.check_currentbalance(Account2)


# In[1]:


import Accounts
import ATM



Account1 = Accounts.Accounts(account_number=123456, account_firstname="Ivan", account_lastname="Villena", current_balance=1000,
                            address="Santolan Pasig", email="villenaic@gmail.com", serial_number="6789")


print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname) 
print(Account1.current_balance) 
print(Account1.address) 
print(Account1.email)
print(Account1.serial_number)


print()

Account2 = Accounts.Accounts(account_number=654321, account_firstname="John", account_lastname="Doe", current_balance=2000,
                            address="Gold Street Quezon City", email="johndoe@yahoo.com", serial_number="4567")

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname) 
print(Account2.current_balance) 
print(Account2.address) 
print(Account2.email)
print(Account2.serial_number)

ATM1 = ATM.ATM()

ATM1.deposit(Account1, 500)
ATM1.check_currentbalance(Account1)

ATM1.deposit(Account2, 300)
ATM1.check_currentbalance(Account2)

ATM1.view_transactionsummary(Account1)
ATM1.view_transactionsummary(Account2)


# In[ ]:





# In[ ]:




