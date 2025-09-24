#WAP to create a class calculator

class calc:
    obj='CALCULATOR'
    def __init__(self,num):
        self.square=(num**2)
        self.cube=(num**3)
        self.root=num**(1/2)
    @staticmethod
    def good():
        print('Hello Dawg')

num=int(input("Enter any number"))
calc.good()
result=calc(num)
print('Square is',result.square,'\nCube is',result.cube,'\nSq Root is',result.root)
