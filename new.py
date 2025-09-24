class employee:
    name='Ishant'
    age=29
    salary=69000

    def getinfo(self):
        print(f'Name is {self.name},age is {self.age},salary is {self.salary}')
    
    @staticmethod
    def stat():
        print('No self parameter required ')

ishant=employee()
ishant.getinfo()       
ishant.stat()