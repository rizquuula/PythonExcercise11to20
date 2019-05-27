key = input("Input some password, separate it by comma: ").split(',')       #Input password by console
#key = 'ABd1234@1,a F1#,2w3E*,2We$$3345'.split(',')         #Example of password given in the excercise
keybox = []
iskey = []
pointa = 0
pointb = 0
pointc = 0
pointd = 0
for onekey in key:
    keybox.append(onekey)
    for each_one in onekey:
        if each_one.islower():      #Detect lowercase
            pointa+=1
        elif each_one.isupper():    #Detect uppercase
            pointb+=1
        elif each_one.isnumeric():  #Detect number
            pointc+=1
        elif each_one=='$' or each_one=='#' or each_one=='@':   #Detect special character
            pointd+=1
        else:
            pass        #Skip the other
    if 6 > len(onekey):     #Minimum length password allowed
        pass    #Skip the password/not to be checking more
    elif len(onekey)> 12:   #Maximum password length allowed
        pass    #Skip the password/not to be checking more
    elif pointa != 0 and pointb != 0 and pointc != 0 and pointd != 0:       #Should get each parameter above
        iskey.append(onekey)        #The real password will be an input to the list
    else:
        pass    #The other will just pass
    pointa = 0  #Reset point to next check for other password
    pointb = 0  #Reset point to next check for other password
    pointc = 0  #Reset point to next check for other password
    pointd = 0  #Reset point to next check for other password
        
print('Some passwords that inputed: ', keybox)
print('The valid password(s) : ', iskey)