#Abenezer Kindie
import socket
from socket import *
ready="The server is ready to recieve: "

#The host/ip address is defined
host="127.0.0.1"

#Prompt the server for port
Port = input("Enter the port: ")

#Create the UDP socket
Socket = socket(AF_INET, SOCK_DGRAM)

#Bind the created socket with the IP and Port
Socket.bind((host,int(Port)))

#The server is ready
print (ready)

#Stays in the loop until quited by the client
while True:

    #Recieve the encoded message entered by the client
    message, clientAddress =Socket.recvfrom(4096)

    #checks the message
    if not message:
        break

    #Prints what the client sends for the server
    print ("client says " + str(message))

    #Changes the message to uppercase and Encode 
    modifiedMessage= message.decode().upper()
    

    #Prints what the server is sending
    print ("Server sending: " + str(message))

    #sends the message to the specified client
    Socket.sendto(modifiedMessage.encode(), clientAddress)
    
