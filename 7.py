#WAP to print line no. of python 

with open('6.html') as f:
    lines=f.readlines()
lineno=1
for line in lines:
    if ('python' in line):
        print ("Yess python is present in line no.",lineno)
        break
    lineno+=1    
        
        
else:
    print("No python isnot present")