from operator import itemgetter, attrgetter

print('Input name, old, score: ')    
database = []
while True:                     #Loop input start here
    print('-->',end='')
    data = input().split(',')
    if data[0]=="":
        print("Done")
        break                   #Break when blank input
    elif (len(data)!=3):
        print("Format input salah(err:B)")
        continue                #create error but still continue
    elif data[0].isalpha()==False or data[1].isdigit()==False or data[2].isdigit()==False:  #check the name
        print("Format input salah(err:C)")
        continue                #create error but still continue
    else:
        database.append(data)   #True condition so the input go to database

print (sorted(database, key=itemgetter(0,1,2)))