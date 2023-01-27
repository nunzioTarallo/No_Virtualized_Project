import socket
import pickle

HOST ="127.0.0.1"
PORT = 65481

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	print(f"Connected by {addr}")

