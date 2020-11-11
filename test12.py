from circular_buffer_module import circular_buffer

buffer = circular_buffer()



def append():
    buffer.add_item(5)
    return 0 

def remove():
    buffer.remove_item()
    return 0