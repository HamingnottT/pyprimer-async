# multiprocessing

from multiprocessing import Process         #imports the library module necessary for multiprocessing
import os                                   #imports os so that python can work with individual system information
import time                                 #optional library import only for calling a timed delay in this example

def example_process():
    # predefine target arguement in Process
    def square_numbers():
        for i in range(100):
            i * i
            time.sleep(0.1)                     #delays process by factor of 10 percent

    processes = []                              #creates template list for processes    
    num_processes = os.cpu_count()              #ensures number of processes don't go above CPU core count

    # create processes

    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start processes
    for p in processes:
        p.start()

    # join processes
    for p in processes:
        p.join()                                #this waits for a process to finish and while waiting for termination of all processes, it is blocking the main thread

    print("end main")

def main():
    print("concurrance.py running. . .")
    example_process()

if __name__ == '__main__':
    main()