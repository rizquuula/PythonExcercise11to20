import re

lines = "hello what a bautifull world at 27 mei 2019 on 19 aclock"              #Input a line of text
striplines = lines.replace(' ','')      #remove any space

output = []
digit = 0
letter = 0
line = lines.split()
for word in line:
        match = re.search(r'\d+.?\d*', word)        #Finding any digit
        if match:
            num = len(match.group())    #Counting
            digit+=num
            
key = len(striplines)       #Total word
letter = key-digit          #Total world - number
print ("LETTERS ",letter)
print ("DIGITS ",digit)