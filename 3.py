#WAP to generate multiplication table from 2 to 20

import os
os.makedirs('tables', exist_ok=True)

def table():
    for n in range (2,21):
        content=''
        for i in range(1,11):
            content += (f'{n} x {i}= {n*i}\n')
        with open(f'tables/table_{n}.txt','w') as f:
            f.write(content)
table()

