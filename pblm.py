list=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

for index,day in enumerate(list):
    while index==2 or index==4 or index==6:
        print(f"Index: {index+1}, Day: {day}")
        break