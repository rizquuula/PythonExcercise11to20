binary = '0100,0011,1010,1001'.split(',') #input binary as a string and split it up
box=[]  #box to store the result
for i in binary:
    num = (int(i,2))        #Convert binary to decimal 
    if (num%5)==0:          #Detecting the number divide-able by 5
        box.append(i)       #input the result to the box
    else:
        pass

print(box)      #printing the result
