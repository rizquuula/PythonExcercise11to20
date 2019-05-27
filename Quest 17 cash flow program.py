print("Input cash flow: ")      #Input d 200 (deposite) or w 222 (withdraw)
blackbox=[]             #Saving storage for number
value=0
while True:             #Looping the input
    print('>',end='')
    data = input()
    if data=='':
        break           #Break when get blank input
    else:
        blackbox.append(data)       #Append the data input to storage

for i in blackbox:
    box = i.split(' ')          #Make new list in the list
    if box[0]=='D' or box[0]=='d':  #Detect first value in the low level list
        value+=int(box[1])      #Counting
    if box[0]=='W' or box[0]=='w':  #Detect first value in the low level list
        value-=int(box[1])      #Counting
    else:
        pass    #For a wrong input, will be ignored
    
print(value)        #Print last value counted
    
