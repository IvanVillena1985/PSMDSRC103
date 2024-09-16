#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math 

def quadratic_formula(a, b, c): 
    if b**2 - (4*a*c) < 0: 
        x1 = (complex(-b, math.floor(math.sqrt(abs(b**2-(4*a*c))))))/2*a
        x2 = (complex(-b, -1*math.floor(math.sqrt(abs(b**2-(4*a*c))))))/2*a
        return x1, x2
              
    else:
        x1 = (-b*math.sqrt(b**2 - (4*a*c)))/(2*a)
        x2 = (-b*math.sqrt(b**2 - (4*a*c)))/(2*a)
        return x1, x2
    
while True:
    a = float(input("Enter a coefficient a:"))
    b = float(input("Enter a coefficient b:"))
    c = float(input("Enter a coefficient c:"))
    
    solutions = quadratic_formula(a, b, c)
    
    print(f"Your answer is: {solutions[1]} and {solutions[-1]}")
    
    file = open("quadratic.txt", "w")
    file.write(f"The solutions are: {solutions[0]} and {solutions[1]}\n")
    file.close() 
    
    print('Your answer was saved!')
    break 


# In[ ]:





# In[ ]:




