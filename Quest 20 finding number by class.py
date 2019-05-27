class Iteration:        #Create a class
    def __init__(self,min,max):
        for i in range(min,max):    #looping
            if i%7==0:              #For multiple of 7
                print(i,end=',')    #Print it

Iteration(0,200)        #Program just launch here
