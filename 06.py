#WAP to print factorial of a number

num=int(input("Enter a number: "))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(f"The factorial of {num} is: {fact}")
    #or
'''num=int(input("Enter a number: "))
fact=1
i=1
for i in range(1,num+1):
    fact=fact*i
print(f"The factorial of {num} is: {fact}")'''