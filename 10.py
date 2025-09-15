#   WAP to print table in reverse order using for loop

n=int(input("Enter the number: "))
for i in range(10,0,-1):
    print(f'{n} x {i} = {n*i}')

              #or

    print(n,'*',i,'=',n*i)