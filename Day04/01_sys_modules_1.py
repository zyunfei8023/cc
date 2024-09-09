
import sys

print(sys.argv)
print(sys.argv[1:])


import time
#时间戳
start = (
    time.time()
)
print(start)#可转换为时间
# time.sleep(1)
#计算时间差
print("duration: {}".format(time.time() - start))

from datetime import datetime

now =datetime.now()
print(now)
print(now.year,now.month,now.day,now.hour,now.minute,now.second)

str_time = datetime.strftime(now,"%Y-%m-%d %H:%M:%S")
print(str_time,type(str_time))

tar_time = datetime.strptime("2024-09-05 12:21:22","%Y-%m-%d %H:%M:%S")
print(tar_time,type(tar_time))
print("-"*10)

arr=[2,3,4,3,5,6,2,1]

print(max(arr))
print(sorted(arr))
print(sorted(arr,reverse=True))
print(arr)

import math

print(math.pow(5,2))

print(math.floor(1.24223))
print(math.ceil(1.24223))
print(round(2.4))
print(round(2.6))

print(math.pi)
print(math.sin(math.pi/6))
print(math.cos(math.pi/3))

import random

print(random.randint(10,20))
print(random.random())
print(random.uniform(1.9,2.5))

lst=[12,12,52,53,2,3,5,6]
print(random.choice(lst))
print(random.choices(lst))





