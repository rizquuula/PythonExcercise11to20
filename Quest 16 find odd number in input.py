#Finding number in input
#Separated by comma
#That cannot divided by 2

key = input("Number: ").split(',')
box = []
for i in key:
    i = int(i)
    if (i%2)!=0:
        box.append(i)
    else:
        pass
print(box)