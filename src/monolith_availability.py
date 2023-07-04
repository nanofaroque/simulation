import numpy as np
import random
import matplotlib.pyplot as plt

MAX_EVENTS= 1000000
def main(total_systems):
    failure= 0
    for i in range(MAX_EVENTS):
        result = []
        for j in range(0,total_systems):
            x = random.randint(0,99) # inclusive; 0..99
            if(x>=99):
                result.append(True)

        # CHECK IF THERE IS A FAILURE IN ANY OF THE SERVICE
        for i in range(0,len(result)):
            if(result[i]==True):
                failure+=1
                break       
    return failure/MAX_EVENTS*100            

if __name__ == "__main__":
    total_iteration = 30
    total_systems = 10
    res_arr = []
    for i in range(1,total_systems+1):
        res=0
        for j in range(total_iteration):
            res += main(i)
        print('outcome: ', res/total_iteration)
        res_arr.append(res/total_iteration)

    print('Final outcome: ', res_arr)    

xpoints = [x for x in range(len(res_arr))]


plt.plot(xpoints, res_arr, 'r--', label='unavailability',
         marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('number of systems or dependencies')
plt.ylabel('Unavailability in %')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()