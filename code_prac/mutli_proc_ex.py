import multiprocessing
import time

def worker_function(name):
    print(f"Worker {name} is starting")
    time.sleep(2)
    print(f"Worker {name} has finished")

if __name__ == "__main__":
    processes = []
    for i in range(4):  # Creating 4 processes
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print("All processes completed.")
