import threading
from circular_buffer_module import circular_buffer
a = circular_buffer()

def add_i(name):
    for i in range(200):
        print(i)
        a.add_item(str(name)+":"+str(i))

def remove(name):
    while a.number_items() > 0: 
        print("thread name:"+str(name)+" = "+str(a.remove_item() )

a1 = threading.Thread(target=add_i,args=(1,))
a2 = threading.Thread(target=add_i,args=(2,))
a3 = threading.Thread(target=add_i,args=(3,))
a4 = threading.Thread(target=add_i,args=(4,))
a5 = threading.Thread(target=add_i,args=(5,))

t1 = threading.Thread(target=remove,args=(1,))
t2 = threading.Thread(target=remove,args=(2,))
t3 = threading.Thread(target=remove,args=(3,))
t4 = threading.Thread(target=remove,args=(4,))
t5 = threading.Thread(target=remove,args=(5,))
#print(type(a1))


# th = [a1,a2,a3,a4,a5]

# print(th)
# th[0].start()

a1.start()
a2.start()
a3.start()
a4.start()
a5.start()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# while True:
#     if a.number_items() == 0:
#         print("consumer = "+str(x))
#         break


# from circular_buffer_module import circular_buffer

# a = circular_buffer()
