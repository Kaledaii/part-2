#WAP to print sum of first n natural numbers using recursion function

def sum(n):
    if n==1:
        return 1
    else:
        return  (n + sum(n-1))
n=int(input("Enter any number "))    
print ('The sum of ',n,'natural no.s is',sum(n))

