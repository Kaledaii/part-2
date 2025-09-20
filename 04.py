#WAP a function to print following pattern 
# ***
# **  
# *

n=int(input("Enter no. of rows "))
def fun(n):
    for i in range(n,0,-1):
        print('*'*i)
    
fun(n)
