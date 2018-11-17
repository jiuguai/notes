from socket import *
import sys

dest = ('<broadcast>',8080)

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.sendto(b'hi',dest)

s.close()