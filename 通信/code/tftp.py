from socket import *

# req_data = '1car.jpg0octet0'
# ack_data = '4block_num'
# err_data = '5err_numinfo0'

import struct
# req_data = struct.pack("!H7sb5sb5sbsb",1,b'car.jpg',0,b'octet',0,b'tsize',0,b'0',0)
req_data = struct.pack("!H5sb5sb",1,b't.mp4',0,b'octet',0)

# print(req_data)
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送请求  
udp_socket.sendto(req_data,('192.168.0.104',69))

with open('t.mp4','wb') as f:
	while True:	
		# 发送请求
		rep_data,addr = udp_socket.recvfrom(516)
		data_len = len(rep_data)
		
		# 获取数据块号
		par = struct.unpack('!HH',rep_data[:4])
		ack_data = struct.pack('!HH',4,par[1])

		# 写入数据
		f.write(rep_data[4:])

		# 向服务器发送收到数据
		udp_socket.sendto(ack_data,addr)

		if data_len < 516:
			break


udp_socket.close()
print('end')


