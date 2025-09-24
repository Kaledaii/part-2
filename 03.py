#WAP to print train no. ,status and fare

from random import randint

class train:
    name="MITHILA EXPRESS"
    print(name,'\n')
    def __init__(self,num):
        self.train_no=num

    def book(self,fro,to):
        print(f'Seat is booked in Train no.{self.train_no} travelling from {fro} to {to}')
    
    def status(self):
        print(f'Train no.{self.train_no} is running on time')

    def fare(self):
        print(f'The ticket costs {randint(245,2005)}')

t=train(149958)
t.book('Nepal','Japan')
t.status()
t.fare()