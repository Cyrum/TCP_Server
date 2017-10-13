import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

server.listen(3)
print "Waiting for connections:"

def client_handler(client):
    response = client.recv(1024);
    if len(response) > 0:
        print "[*] Response from client:", response
    message = raw_input("Write your message: ")
    client.send(message)
    client.close()

while True:
    client, address = server.accept()
    if len(address) > 0:
        print "[*] Connected to : %s:%d" % (address[0], address[1])

    handler = threading.Thread(target=client_handler, args=(client,))
    handler.start()

