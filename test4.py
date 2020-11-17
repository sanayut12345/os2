# from threading import Thread
import time

# def pprint(name):
#     while True:
#         print(f"{name} : hello world")
#         time.sleep(1)

# for i in range(10):
#     t1 = Thread(target = pprint , args = ('Thread-'+str(i),)) 
#     t1.start()

import threading
sem = threading.Semaphore()

global x
x = 0

global buff
buff = []

def fun(n):
    global x
    global buff
    con = 0
    while True:
        
        if x >= 1000:
            sem.acquire()
            buff.append(con)
            sem.release()
            print(f'refer rence counter while = {con}')
            break
        con = con+1
        
        sem.acquire()        
        x = x+1
        print(f'function {n} x = {x}')
        sem.release()
        time.sleep(0.01)

for i in range(10):
    t = threading.Thread(target = fun,args=(i,))
    t.start()
    if (i == 9):
        t.join()

print(f'sum {sum(buff)}')