#WAP to make a copy of a file 

with open('8.txt') as f:
    content=f.read()

with open('copy.txt','w') as f:
    f.write(content)
    
import os
os.remove('8.txt')
