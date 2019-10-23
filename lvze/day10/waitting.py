from select import select
from socket import *
import os

sockfd = socket()
ADDR = ("127.0.0.1",8888)
sockfd.listen(3)

f = open('test','w+')
print('监控IO')

rs,ws,xs = select([s],[],[])
print('rlist',rs)
print('wlist:',ws)
print('xlist:',ws)





