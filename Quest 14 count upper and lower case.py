#Counting uppercase and lowecase

text = input("Input text: ")
upp=0
low=0
for t in text:
    if t.isupper():
        upp+=1
    elif t.islower():
        low+=1
    else:
        pass

print('UPPER CASE ',upp)
print('LOWER CASE ',low)
