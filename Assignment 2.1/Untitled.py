#!/usr/bin/env python
# coding: utf-8

# In[20]:


#defining the greeting through the input function
def greet(first_word, second_word): 
    greetings = f"{first_word} {second_word}"
    return greetings.title()

#creating a list of some bad words. Can be modified by adding other bad words
bad_words = ['fu', 'bs']

#filter the greetings by replacing them with "*"
def censor(text): 
    for word in bad_words:
        text = text.lower().replace(word.lower(), '*****')
    return text

#the while loop is used here to ask the user to enter their name. The break statement enables them to exit the loop after 
#the prompt. Omitting the 'break' results to an infinite loop 
while True: 
    print("\nGreet your classmates today by saying your name and Good Morning:")
    
    name = input("Name:")
    name = censor(name) #inserted the def censor to filter
    
    s_word = input("Type Good Morning:")
    s_word = censor(s_word) #inserted the def censor to filter
    
    censored_greet = greet(name, s_word) #filtered greetings 
    
    print(f"\nHello I am {name} and {s_word}!")
    break #do not omit when while loop is used
    
    


# In[ ]:





# In[19]:





# In[ ]:




