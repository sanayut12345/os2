x = input("# buff ").split(" ")

producer_thread = int(x[0])
consumer_thread = int(x[1])
buffer_size = int(x[2])
request_number = int(x[3])

print(f"Producers {producer_thread}, Consumers {consumer_thread}")
print(f"Buffer size {buffer_size}")
print(f"Requests {request_number}")

#start code multithreading

#end code multithreading
