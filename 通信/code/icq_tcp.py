import socket
from threading import Thread

def recvData(cli):
	while True:
		recv_data = cli.recv(1024)
		if len(recv_data) > 0:
			print('\r>> %s' %(recv_data.decode('gbk')),'\n<<',end='')
		else:
			break
	cli.close()

def sendData(cli):
	while True:
		send_data = input('<<')
		cli.send(send_data.encode('gbk'))

def new_con(ser):
	while True:
		cli, con = ser.accept()
		tr = Thread(target=recvData,args=(cli,))
		ts = Thread(target=sendData,args=(cli,))
		tr.start()
		ts.start()



def main():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind(('192.168.0.51',8080))
	server.listen(5)
	st = Thread(target=new_con,args=(server,))
	st.start()
	st.join()
	server.close()

if __name__ == '__main__':
	main()