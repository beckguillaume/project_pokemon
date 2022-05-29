# pokemon_socket #################
##################################
##### SERVER #####################
##################################

import socket
from time import sleep

JOUEURS_LIST=[]
num_player=0
exit=0
data_utf=""
msg=""

#création d'un socket INET (=IPV4), STREAM (=TCP)
# socket serveur recevant les commandes de modification de la BDD
# et la communication entre les joueurs
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#permet de réutiliser l'adresse même avec des exécutions consécutives du script
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
    c=0
    while c == 0 :
        try:
            (clientsocket, address) = serversocket.accept()
            c = 1
        except:
            print("En attente des joueurs...")
            sleep(2)
    # print(type(clientsocket))
    print("Un nouveau combattant approche... => ",address)
    JOUEURS_LIST.append(clientsocket)
    #print("dans la boucle while")
    # print("La liste => ",JOUEURS_LIST)

for i in range(len(JOUEURS_LIST)):
    #print("dans la boucle for")
    msg="Connexion du joueur "+str(i+1)+" "+str(address)
    print(msg)
    msg="Tous les joueurs sont connectés, la partie peut commencer ! Vous êtes le joueur "+str(i+1)
    JOUEURS_LIST[i].send(msg.encode('utf-8'))
    sleep(0.5)
    JOUEURS_LIST[i].send(str(i).encode('utf-8'))

#boucle principale. La variable num_player permet ici d'alterner entre deux clients. 
num_player=0
exit=0
while exit == 0 :

    #exemple d'utilisation : chat entre 2 sockets clients
    #le socket server reçoit les messages et les transfère vers l'autre client

    data = JOUEURS_LIST[num_player].recv(1024)
    data_utf=data.decode('utf-8')
    print(data_utf)
    
            # lignes pour modifier un fichier bdd :
                # with open("bdd_test",'a') as f:
                #     f.write(data_utf)
                #     f.close()
        
    # si émetteur = socket client 1, on envoie à socket client 2
    if num_player == 0 :
        num_player+=1
        JOUEURS_LIST[num_player].send(data)
        if data.decode('utf-8') == 'exit':
            exit=1
    # si émetteur = socket client 2, on envoie à socket client 1
    else :
        num_player-=1
        JOUEURS_LIST[num_player].send(data)
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