from threading import Thread
from time import sleep
from event_module import event

global a
a = event()

def Sleep():
    d = a.sleep(2)
    print("sleep = ",d)

def wakeup():
    sleep(1)
    a.wake_up()

sl = Thread(target=Sleep)
wk = Thread(target=wakeup)
sl.start()
wk.start()
wk.join