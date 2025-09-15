#WAP to print star pattern
# *
# **
# ***

n=3

for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
 #or
for i in range(n):
    print('* '*(i+1))
    