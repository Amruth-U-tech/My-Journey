'''this is a code for parallel programing for matrix multiplication 
which can be used in computer vision algorithms'''
import time
import multiprocessing as mp

n = 1000
A = [[2.0 for _ in range(n)] for _ in range(n)]
x = [1.0 for i in range(n)]

def compute_row(i):
    total = 0
    for j in range(n):
        total += A[i][j]*x[j]
    return total

if __name__=="__main__":
    print(f"intialisation of the matrix {n}x{n}")

    start = time.perf_counter()
    with mp.Pool() as pool:
        Y = pool.map(compute_row,range(n))
    end  = time.perf_counter()

    print("computation completed")
    print(Y)
    print(f"\nexcution time: {end-start}s.")
    '''//'''