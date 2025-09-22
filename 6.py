with open('6.html') as f:
    content=f.read().lower()
if('python' in content):
    print("Yes python is present")
else:
    print("No python isnot present")