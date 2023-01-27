import socket


HOST ="127.0.0.1"
PORT1 = 65480
PORT2 = 65481
PORT3 = 65482

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
	s1.connect((HOST,PORT1))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
	s2.connect((HOST,PORT2))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s3:
	s3.connect((HOST,PORT3))


