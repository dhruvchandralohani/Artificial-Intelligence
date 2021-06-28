import socket

x= socket.socket()
h_name= input(str("Enter the hostname of the server"))
port = 8080

x.connect((h_name,port))
print("Connected to chat server")

while 1: 
   incoming_message=socket.recv(1024)
   incoming_messagge=incoming_message.decode()
   print(" Server :", incoming_message)
   message= input(str(">>"))
   Message =message.encode()
   socket.send(Message)
   print(" message has been sent...")