f=open('poem.txt')
d=f.read()
if('twinkle'in d or 'Twinkle'in d  ):
    print("Yess Twinkle is present in the poem")
else:
    print("Noo Twinkle isnot present in the poem")
f.close()
