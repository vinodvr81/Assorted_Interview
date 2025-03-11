from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def worker_function(name):
    print(f"Worker {name} is starting")
    time.sleep(2)
    print(f"Worker {name} has finished")
    return f"Worker {name} result"

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(worker_function, i) for i in range(4)]
        for future in as_completed(futures):
            print(future.result())
    print("All threads completed.")
