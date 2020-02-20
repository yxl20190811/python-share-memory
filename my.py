import multiprocessing
from multiprocessing import Process,Manager

import time

def run_add(value):
    for i in range(1,999999999999):
        value.value = 1;
        time.sleep(2)

def run_clear(value):
    for i in range(1,999999999999):
        value.value = 2;
        time.sleep(5)


if __name__ == '__main__':

    processes = list()

    value = multiprocessing.Value('i', 0)
    p = Process(target=run_add, args=(value,))
    p.start()
    processes.append(p)

    p = Process(target=run_clear, args=(value,))
    p.start()
    processes.append(p)

    for i in range(1,999999999999):
        print(value.value)
        time.sleep(2)

    for p in processes:
      p.join()
    print('Process end.')