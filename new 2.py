# -*- coding: utf-8 -*-
# import os # 导入os模块，模块的概念后面讲到
# print([d for d in os.listdir('..')]) # os.listdir可以列出文件和目录

#generator

# def fib(max):
    # n,a,b = 0,0,1
    # while n < max:
        # yield(a)
        # a,b = b,a+b
        # n+=1
        
# for n in fib(10):
    # print(n)

# def is_odd(n):
    # return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# print(list(filter(lambda x: x%2==1,range(1,20))))


# import time, functools

# def metric(fn):
    # print('%s executed in %s ms' % (fn.__name__, 10.24))
    # return fn
    
# @metric
# def fast(x, y):
    # time.sleep(0.0012)
    # return x + y
    
# print(fast(11,22))

from canlib import canlib

num_channels = canlib.getNumberOfChannels()
print("Found %d channels" % num_channels)
for ch in range(0, num_channels):
    chdata = canlib.ChannelData(ch)
    print("%d. %s (%s / %s)" % (ch, chdata.channel_name,
                                chdata.card_upc_no,
                                chdata.card_serial_no))