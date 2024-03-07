#Python Multiprocessing Tutorial: Run Code in Parallel Using the Multiprocessing Module

'''
use threading para operações I/O-bound que não exigem 
muito processamento intensivo, e use multiprocessamento 
para tarefas que podem se beneficiar da execução paralela
em múltiplos núcleos de CPU, especialmente se forem 
intensivas em CPU.
'''
import concurrent.futures
import multiprocessing
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} second(s)'

if __name__ == '__main__':
    start = time.perf_counter()

    # Using multiprocessing.Process
    p1 = multiprocessing.Process(target=do_something, args=[1])
    p2 = multiprocessing.Process(target=do_something, args=[1])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # Using concurrent.futures.ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
