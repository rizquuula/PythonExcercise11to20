#This program print all number that can divided by 2
#ex: 2000,2440,2446

box=[]
for i in range(1000,3001):
    x = str(i)
    if (int(x[0])%2==0 and int(x[1])%2==0 and int(x[2])%2==0 and int(x[3])%2==0 ):
        box.append(x)
    else:
        pass
for i in box:
    print(i,end=(','))      #Printing in a line, separated by ','