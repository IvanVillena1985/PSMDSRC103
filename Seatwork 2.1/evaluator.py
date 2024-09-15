#!/usr/bin/env python
# coding: utf-8

# In[39]:


print('Propositional Logic Evaluator for Discrete Math')
variables = int(input('How many variables:'))
total_combinations = 2 ** variables

combinations_list = []


# In[40]:


for i in range(total_combinations):
    bin_equivalent = bin(i)[2:]
    while len(bin_equivalent) < variables:
        bin_equivalent = '0'+bin_equivalent
    combinations_list.append(tuple(int(val) for val in bin_equivalent))


# In[41]:


expression = input('Enter the propositional logic expression:') #A, B and C only and must be in small cases


# In[43]:


if variables == 2: 
    print('A B f')
    for A, B in combinations_list: 
        evaluated_expression = eval(expression)
        print(A, B, evaluated_expression)
elif variables == 3: 
    print("A B C f")
    for A, B, C in combinations_list: 
        evaluated_expression = eval(expression)
        print(A,B,C, evaluated_expression)


# In[ ]:




