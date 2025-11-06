list=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

for index,day in enumerate(list):
    index+=1
    while index==3 or index==5 or index==7:
        print(f" {index}, Day: {day}")
        break