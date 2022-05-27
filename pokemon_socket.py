# pokemon_socket #################
##################################
##### SERVER #####################
##################################
import socket
from time import sleep
i=0
JOUEURS_LIST=[]
exit=0
data_utf=""
msg=""

# create an INET (=IPV4), STREAM (=TCP) socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.settimeout(0)

#serversocket.setblocking(False)
#serversocket.type(socket.SOCK_NONBLOCK)

# bind the socket to a public host, and a well-known port
serversocket.bind(('', 8888))

# become a server socket
serversocket.listen()

# accept connections from outside until we have enough players
while len(JOUEURS_LIST) < 2:
    c=True
    while c == True:
        try:
            (clientsocket, address) = serversocket.accept()
            c=False
        except:
            print("connecting.....")
            sleep(1)
    # print(type(clientsocket))
    print("Nouvelle co=> ",address)
    JOUEURS_LIST.append(clientsocket)
    print("dans la boucle while")
    # print("La liste => ",JOUEURS_LIST)
for i in range(len(JOUEURS_LIST)):
    print("dans la boucle for")
    print(i)
    msg=["Connexion du joueur",i+1,address]
    print(str(msg))
    msg="Tous les joueurs sont connectés, la partie peut commencer !"
    JOUEURS_LIST[i].send(str(msg).encode('utf-8'))

i=0
while exit == 0:
    #for i in range(len(JOUEURS_LIST)):
    data = JOUEURS_LIST[i].recv(1024)
    data_utf=data.decode('utf-8')
    print(data_utf)
    
    # on agit sur la bdd
    # with open("bdd_test",'a') as f:
    #     f.write(data_utf)
    #     f.close()
        
    # on redirige vers l'autre user
    if i == 0:
        i+=1
        JOUEURS_LIST[i].send(data)
        if data.decode('utf-8') == 'exit':
            exit=1
    else:
        i-=1
        JOUEURS_LIST[i].send(data)
        if data.decode('utf-8') == 'exit':
            exit=1
        
            
#################
#    " else:
#         msg=input()
#         clientsocket.send(msg.encode('utf-8'))
#         if msg == "exit":
#             exit=1"
####
# if data.decode('utf-8') == 'hello world':
#    clientsocket.send(str('Tango Charly, je repete: Tango Charly').encode('utf-8'))
##################

# Closing socket
clientsocket.close()
serversocket.close()