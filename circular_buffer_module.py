#############################   Credit  #############################
#########################   writed by Art   #########################
##################    email sanayut12@gmail.com   ###################
####################    date writed 10/24/2020  #####################


class circular_buffer:      
    def __init__(self,buffer_size):
        self.top = 0        #top of circular buffer
        self.botton  = 0    #botton of circular buffer
        self.buffer = []    #init buffer
        self.buffer_size = buffer_size   #size of buffer
        for i in range(self.buffer_size):    #set size of buffer by append item in array becouse python not set of size array or list
           self.buffer.append(None)     #add items into array

    # focus
    def add_item(self,item):    #methode >>use add item into buffer
        if self.buffer[self.botton] == None:
            self.buffer[self.botton] = item
            self.botton += 1
            if self.botton >= self.buffer_size:         #if buffer overflow   
                self.botton = 0
        else:
            print("over item")
            return None

    def remove_item(self):
        if self.buffer[self.top]  != None:
            data = self.buffer[self.top] 
            self.buffer[self.top] = None
            self.top += 1
            if self.top >= self.buffer_size:
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

    #check buffer size
    def check_len(self):
        print("len of array : ",len(self.buffer))
        
    def number_items(self):
        number = 0
        for i in range(len(self.buffer)):
            i = self.buffer[i]
            if i != None:
                number += 1
        #print("number in buffer : ",number)
        return number
##how to use!###
#from circular_buffer_module import circular_buffer
#a = circular_buffer(1000) #begin function
#a.add_item(50)# 50 is items
#result = a.remove_item() # has return value