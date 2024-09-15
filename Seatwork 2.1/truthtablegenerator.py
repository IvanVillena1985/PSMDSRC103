#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def generate_truthtable(number_of_variables):
    total_combinations = 2 ** number_of_variables
    combinations_list = []
    
    for i in range(total_combinations):
        bin_equivalent = bin(i)[2:]
        while len(bin_equivalent) < number_of_variables: 
            bin_equivalent = "0"+bin_equivalent
    combinations_list.append(tuple(int(val) for val in bin_equivalent))
    return combinations_list  


# In[ ]:


print(generate_truthtable(3))


# In[ ]:


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


def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0: 
        return "You need to enter an integer"
    else:
        total_combinations = 2 ** number_of_variables
        combinations_list = []
        
        for i in range(total_combinations): 
            bin_equivalent = bin(i)[2:]
            while len(bin_equivalent) < number_of_variables: 
                bin_equivalent = "0"+bin_equivalent
            combinations_list.append(tuple(int(val) for val in bin_equivalent))
        return combinations_list


# In[ ]:


print(generate_truthtable())


# In[ ]:


expression = input('Enter the propositional logic expression:') #A, B and C only and must be in small cases


# In[ ]:


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


evaluate_propositional_logic(generate_truthtable(3))


# In[ ]:





# In[ ]:




