from circular_buffer_module import circular_buffer
from threading import Thread
from time import sleep,time


number_productor = 5
number_consumer = 5
buffer_size = 100
request_number = 1000
lock = 0
buffer = circular_buffer(buffer_size)

count = 0
size = buffer_size

def append(thread_name,lock,request_number,buffer_size):
    while True:
        #print("append")
        if buffer.number_items == buffer_size:
            sleep(1)
        if lock == 0:
            lock = 1

            #start critical region
            buffer.add_item("x")
            #stop critical region
            sleep(0.1)
            request_number = request_number - 1
            if(request_number == 0):
                break

            lock = 0        
        break

def remove(thread_name,lock,count):
    while True:
        print("remove")
        if lock == 0:
            lock = 1
            #start critical region
            item = buffer.remove_item()
            count = count + 1
            #stop critical region
            sleep(0.1)
            lock = 0
            if buffer.number_items == None:
                break
            if item == 'x':
                count = count + 1


start = time()
productor_thread = Thread(target=append,args=("Productor : "+str(1),lock,request_number,buffer_size))
productor_thread.start()
productor_thread.join()
end = time()
print(end-start)

#create thread productor
# for i in range(number_productor):
#     productor_thread = Thread(target=append,args=("Productor : "+str(i+1),lock,request_number,buffer_size))
#     productor_thread.start()
#     productor_thread.join()



#create thread consumer
# for i in range(number_consumer):
#     consumer_thread = Thread(target=remove,args=("Consumer : "+str(i+1),lock))
#     consumer_thread.start()
#     consumer_thread.join()

