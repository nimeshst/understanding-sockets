import  socket 

import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))


while True:
    full_message = b''
    new_message = True
    while True:
        message = s.recv(16)# how many chunk of data we will receive 
        if new_message :
            print('new message lenght',message[:HEADERSIZE])
            msg_length = int(message[:HEADERSIZE])
            new_message = False
        print(f'full messagelength :{msg_length}')

        
        full_message += message
        
        print(len(full_message))

        if len(full_message)-HEADERSIZE == msg_length:
            print('full message recived')
            print(full_message[HEADERSIZE:])
            
            d = pickle.loads(full_message[HEADERSIZE:])
            print(d)

            new_message = True
            full_message = b''
    print(full_message)
