#WAP to greet all the person names starting with S

l=["Harry","soham","Rohan","Shubham"]

for i in l:
    if i.startswith('S') or i.startswith('s'):
        print("Hello",i)
          #or
    if i[0].lower()=='s':
     print("Hello",i)