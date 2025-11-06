class Employee:
    def __init__(self):
        print("Constructor employee")
    
class Coder:
    def __init__(self):
        print("Constructor coder")

class Manager(Employee, Coder):
    def __init__(self):
        super().__init__()
        Coder.__init__(self)

        print("Constructor manager")


c=Manager()