'''this program is to use parrale programing in python for using it in ml application,and fast programing'''

import time
import os
import multiprocessing as mp

'''this code is to compare static sheduling and dynamic sheduling'''

def work(i):
    time.sleep(0.1*(i%3))
    print(f"process {os.getpid()} processing iterations {i}")

if __name__=="__main__":
    iterations = list(range(20))
    num_cores = mp.cpu_count()
    
    print("-------------static sheduling------------------")
    with mp.Pool(processes=num_cores) as pool:
        pool.map(work,iterations)

    print("\n-------------dynamic sheduling-----------------")
    with mp.Pool(processes=num_cores) as pool:
        pool.map(work,iterations,chunksize=1)
        