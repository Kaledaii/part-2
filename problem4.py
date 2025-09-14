# Write a Python program to print the contents of a directory using OSModule.

# select drive whose content u want to print 
import os

# checks the contents of that drive 
for item in os.listdir('E:\\'):
 
#    prints the content of that drive 
    print(item)


  