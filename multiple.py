class emp:
    name="Ramesh"
    def pr(self):
        print(f'The name of employee is {self.name}')

class detail:
    adress="HTD-2"
    def dtl(self):
        print(f"You live in {self.adress}")

class company(emp,detail):
    cmp="EduTech"
    language='Python'
    def lang(self):
        print(f'Nigga your language is {self.language} in our company {self.cmp}')

a=emp()
b=detail()
c=company()
print(a.name,b.adress,c.cmp,c.language)
c.pr()
c.dtl()
c.lang()
