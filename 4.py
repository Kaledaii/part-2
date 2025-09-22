word= 'donkey'
with open('4.txt') as f:
    content =f.read().lower()
    content=content.replace(word,'####')
with open('4.txt','w') as f:
    f.write(content)
   

