class student:
    name="raj"
    roll=55

    def __init__(self, stud, roll):
        self.name=stud
        self.roll=roll
    
raj=student('raj',99)
print(raj.name,raj.roll)