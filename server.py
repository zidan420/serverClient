import socket
from threading import Thread

IP = '0.0.0.0'
PORT = 9998

def handle_client(client):
	with client as sock:
		request = sock.recv(4096)
		print(f'[*] Received: {request.decode("utf-8")}')
		sock.send(b'ACK')

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT))

	server.listen(2)
	print(f"Listening on {IP}:{PORT}")

	try:
		while True:
			client, address = server.accept()
			print(f'[*] Accepted connection from {address[0]}:{address[1]}')
			t = Thread(target=handle_client, args=(client,))
			t.start()
	except:
		print("Closing Server..")
		server.close()

if __name__ == '__main__':
	main()