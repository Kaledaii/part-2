#WAP to check prime number

num=int(input("Enter a number: "))
a=0
for i in range(2,num):
    if num%i==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")

      #or

''' if num%i==0:
        a+=1
if a==0:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")'''