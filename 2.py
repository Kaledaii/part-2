#Create a class 'pets' from class 'Animals' and further create a class 'Dogs' from class 'pets'. Add a method 'bark' in class 'Dogs' which prints "Woof Woof".

class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Woof Woof")
   

a=Dogs()
a.bark()
