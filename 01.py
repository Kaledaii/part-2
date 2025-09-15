#WAP to print multiplication table

num=int(input("Enter a number: "))

for i in range(1,11):
    #Either one , both are correct
    print(num,'*',i,'=',num*i)
        #or
    print(f"{num}*{i}={num*i}")
    