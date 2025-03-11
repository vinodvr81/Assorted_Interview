import threading
import time

def worker_function(name):
    print(f"Worker {name} is starting")
    time.sleep(2)
    print(f"Worker {name} has finished")

if __name__ == "__main__":
    threads = []
    for i in range(4):  # Creating 4 threads
        thread = threading.Thread(target=worker_function, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("All threads completed.")
