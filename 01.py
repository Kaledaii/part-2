#WAP to create a class to store a name of few programmers working at microsoft

class dev:
    company="Microsoft"
    
    def __init__(self,name,adress,salary):
        self.name=name
        self.adress=adress
        self.salary=salary
pg=dev('Kale','ohio',330000)
print(pg.company,pg.name,pg.adress,pg.salary)
pg=dev('Gore','L.A',455000)
print(pg.company,pg.name,pg.adress,pg.salary)


