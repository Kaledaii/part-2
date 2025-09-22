words=['nigga','bitch','w']

with open('5.txt') as f:
    content=f.read().lower()

for word in words:
    content=content.replace(word, '#'*len(word))
with open('5.txt','w') as f:
    f.write(content)