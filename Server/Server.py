from cgitb import html
from socket import *
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 80

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
        print('Waiting for requests ...')
        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()
        try:
                message = connectionSocket.recv(1024)
                # -------------------------------------------
                #       Request handling Section
                # -------------------------------------------
                data_received=message.split(b'\r\n')
                for i in range(len(data_received)):
                        print(data_received[i]) # Q1 we iterate through "data_received" and print its content
                        if i == 0:
                                #Q2 we split the first line (GET line) and take the second index to get the request URL
                                GETData = data_received[i].split()
                                requested_resource = GETData[1]
                
                # for only_text.html http://127.0.0.1:80/server/hemsidan/HTML/Log_in.html
                # We recive two requests the first one is the only_text.html and the second one is for faviocon.ico
                # and the browser displays the given html code


                #open and sends the requsted file.
                f = open(requested_resource[1:],'rb')
                outputdata = f.read()
                connectionSocket.sendall(outputdata)

                connectionSocket.close()

        except IOError:
                # ----------------------------------
                #       I/O Error handling
                # ----------------------------------
                        connectionSocket.close()
        except IndexError:
                print('Index error exception')                          
serverSocket.close()   