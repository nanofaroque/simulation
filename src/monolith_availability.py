import numpy as np
import random

MAX_EVENTS= 100000
MAX_NUMBER_SYSTEMS = 3
def main():
    failure= 0
    for i in range(MAX_EVENTS):
        result = []
        for j in range(0,MAX_NUMBER_SYSTEMS):
            print('value of j: ', j)
            x = random.randint(0,99) # inclusive; 0..99
            print('value of x: ', x)
            if(x>=99):
                result.append(True)
                print('got it: ',x)

        # CHECK IF THERE IS A FAILURE IN ANY OF THE SERVICE
        for i in range(0,len(result)):
            if(result[i]==True):
                failure+=1
                break       
    print('value: ', failure/MAX_EVENTS*100)            


if __name__ == "__main__":
    main()
