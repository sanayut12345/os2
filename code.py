#class file  circular buffer

#size of buffer
buffer_size = 1000
class circular_buffer:      
    def __init__(self):
        self.top = 0        #top of circular buffer
        self.botton  = 0    #botton of circular buffer
        self.buffer = []    #init buffer
        for i in range(buffer_size):    #set size of buffer by append item in array becouse python not set of size array or list
           self.buffer.append(None)     #add items into array
    
    #check buffer size
    def check_len(self):
        print("len of array : ",len(self.buffer))

    # focus
    def add_item(self,item):    #methode >>use add item into buffer
        if self.buffer[self.botton] == None:
            self.buffer[self.botton] = item
            self.botton += 1
            if self.botton >= 1000:         #if buffer overflow   
                self.botton = 0
        else:
            print("over item")
            return None

    def remove_item(self):
        if self.buffer[self.top]  != None:
            data = self.buffer[self.top] 
            self.buffer[self.top] = None
            self.top += 1
            if self.top >= 1000:
                self.top = 0
            return data
        else:
            print("none item")
            return None

    def get_top(self):
        print("top of buffer : ",self.top)

    def get_botton(self):
        print("botton of buffer : ",self.botton)

    def show_items(self):
        print("item all => ",self.buffer)

    def number_items(self):
        number = 0
        for i in range(len(self.buffer)):
            i = self.buffer[i]
            if i != None:
                number += 1
        #print("number in buffer : ",number)
        return number


# file test class circular buffer

import threading
from circular_buffer_module import circular_buffer
a = circular_buffer()

def add_i(name):
    for i in range(200):
        print(i)
        a.add_item(str(name)+":"+str(i))

def remove(name):
    while a.number_items() > 0: 
        print("thread name:"+str(name)+" = "+str(a.remove_item()))

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
print(type(a1))


th = [a1,a2,a3,a4,a5]

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

    
