#############################   Credit  #############################
#########################   writed by Art   #########################
##################    email sanayut12@gmail.com   ###################
####################    date writed 10/24/2020  #####################
buffer_size = 1000
class circular_buffer:      
    def __init__(self):
        self.top = 0
        self.botton  = 0
        self.buffer = []
        for i in range(buffer_size):
           self.buffer.append(None) 
    
    def check_len(self):
        print("len of array : ",len(self.buffer))

    def add_item(self,item):
        if self.buffer[self.botton] == None:
            self.buffer[self.botton] = item
            self.botton += 1
            if self.botton >= 1000:
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

##how to use!###
# print("aaaa")
# a = circular_buffer()
# a.check_len()