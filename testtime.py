import datetime
from time import sleep,time
x = 0
start = time()
for i in range(1000000):
    x = x+1
#sleep(1)
end = time()
print(end-start)
print(x)