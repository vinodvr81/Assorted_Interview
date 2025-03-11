import multiprocessing
import time

def worker_function(name):
    print(f"Worker {name} is starting")
    time.sleep(2)
    print(f"Worker {name} has finished")

if __name__ == "__main__":
    process = []
    for i in range(4):  # Creating 4 threads
        proc = multiprocessing.Process(target=worker_function, args=(i,))
        process.append(proc)
        proc.start()

    for proc in process:
        proc.join()
    print("proc threads completed.")
