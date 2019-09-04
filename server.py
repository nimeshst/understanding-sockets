# server
import socket
import pickle 



HEADERSIZE = 10
# create an INET, STREAMing socket
s= socket.socket(socket.AF_INET # Family type corresponds to IPv4
        , socket.SOCK_STREAM)
# bind the socket to the public host
s.bind((socket.gethostname(),1234))
# listen specifies how many socket library that we want 
# before refusing outside connection
s.listen(5)

while True :
    # accept the connection from outside
    clientsocket , address = s.accept()
    
    print(f"connection from  {address}")
    
    d = {1:"hey",2:"hiii"}

    message = pickle.dumps(d)
    
    message = bytes(f'{len(message):<{HEADERSIZE}}',"utf-8")+message

    
    clientsocket.send(message)
    # close the connection
