from threading import Thread
from socket import *

def sendData(addr,udp_socket):
    while True:
        data = input('<<')
        udp_socket.sendto(data.encode('gbk'),addr)

def recvData(udp_socket):
    while True:
        data = udp_socket.recvfrom(1024)
        print('\r>>%s:%s' %(data[1],data[0].decode('gbk')),'\n<<',end='')



def main():

    udp_socket = socket(AF_INET,SOCK_DGRAM)
    bind_addr = ('',8081)
    udp_socket.bind(bind_addr)
    target_ip = '192.168.0.51'
    target_port = 8080
    # target_ip = input('目標端的IP地址:')
    # target_port = int(input('目標端端口號:'))

    ts = Thread(target=sendData,args=((target_ip,target_port),udp_socket))
    tr = Thread(target=recvData,args=(udp_socket,))

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == '__main__':
    main()
