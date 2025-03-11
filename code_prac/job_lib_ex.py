from joblib import Parallel, delayed
import time

def worker_function(name):
    print(f"Worker {name} is starting")
    time.sleep(2)
    print(f"Worker {name} has finished")

if __name__ == "__main__":
    Parallel(n_jobs=4)(delayed(worker_function)(i) for i in range(4))
    print("All jobs completed.")
