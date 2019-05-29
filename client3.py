#Abenezer Kindie
import socket

#Prompt the client for IP
host = input("Enter the IP : ")

#Prompt the client for port
port = input("Enter the port: ")

#Attach to the UDP socket
Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Prompt the client for message
message =input("Please enter the statement: ")

#Stays in the loop until quited by the client using the 'q' key
while (message!="q"):

        #Encode the message then sends the message through the given ip and port
        Socket.sendto(message.encode(),(host, int(port)))

        #Recieve the uppercased message from the server
        modifiedMessage, serverAddress =Socket.recvfrom(4096)

        #Decode the message and then prints 
        print ("Returned text from the server: "+modifiedMessage.decode())
        
        print("Type q to quit !! ")
        
        message =input("Please enter the statement: ")

print("Ooops....You quited")

#IF out of the ;oop, the socket is closed
Socket.close() 
 
