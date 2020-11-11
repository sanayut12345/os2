from circular_buffer_module import circular_buffer

producer_thread = 5
consumer_thread = 5
buffer_size = 100
request_number = 1000


buffer = circular_buffer(buffer_size)


def append():

    #start critical region
    buffer.add_item(5)
    #stop critical region


def remove():

    #start critical region
    buffer.remove_item()
    #stop critical region
