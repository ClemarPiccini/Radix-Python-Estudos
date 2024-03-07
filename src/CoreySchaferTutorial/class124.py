#Python Threading Tutorial: Run Code Concurrently Using the Threading Module
import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# Criar uma lista de threads
threads = []

# Criar e iniciar 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

# Esperar todas as threads terminarem
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
