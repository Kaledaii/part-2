class pg:
    name="Ramesh"
    def pr(self):
        print(f'The name of employee is {self.name}')

class company(pg):
    cmp="EduTech"
    language='Python'
    def lang(self):
        print(f'Nigga your language is {self.language} in our company {self.cmp}')

a=pg()
b=company()
print(a.name,b.cmp,b.language)
b.pr()
b.lang()