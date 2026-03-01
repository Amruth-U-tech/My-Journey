import time
import multiprocessing as mp

def chunk_sum(chunk):
    return sum(chunk)
def main():
    n = 1000000
    arr = [1]*n
    print("-----------------------------------\n")
    #Serial execution
    print("executing serial algorithm.......")
    start = time.perf_counter()
    total_serial = sum(arr)
    end = time.perf_counter()
    total_serial_time = end-start
    print("-----------------------------------\n")

    #parallel execution
    print("Executing parallel algorithm.......")
    num_of_cores = mp.cpu_count()
    pool = mp.Pool(processes=num_of_cores)
    chunk_size = n//num_of_cores
    chunks_collected = [arr[i:i+chunk_size] for i in range(0,n,chunk_size)]
    print(f"the no. of cores you have-{num_of_cores}\n size of chunks for available cores is-{chunk_size}")

    start = time.perf_counter()
    partial_sums = pool.map(chunk_sum,chunks_collected)
    total_of_partial_sum = sum(partial_sums)
    end = time.perf_counter()
    pool.close()
    pool.join()
    total_parallel_time = end-start
    print("-----------------------------------\n")
    speed_up = total_serial_time/total_parallel_time
    effeciency = speed_up/num_of_cores

    #results printed
    print(f"total time taken by serial execution is-{total_serial_time}s")
    print(f"total time taken by the parallel execution is-{total_parallel_time}s")
    print(f"speed up - {speed_up}\neffeciency is = {effeciency}")

if __name__ == "__main__":
    mp.freeze_support()
    mp.set_start_method("spawn",force=True)
    main()