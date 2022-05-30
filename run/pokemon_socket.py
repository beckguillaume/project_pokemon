# pokemon_socket #################
##################################
##### SERVER #####################
##################################
'''
pokemon_socket contient les fonctions permettant d'implémenter 
les sockets dans script_partie1.
'''

import socket
from time import sleep

#fonction de création du socket serveur. 
# Cette fonction est appelé par le script principal à l'initialisation de la partie.

def create_server_socket() :

    JOUEURS_LIST=[]

    #création d'un socket INET (=IPV4), STREAM (=TCP)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #permet de réutiliser l'adresse même avec des exécutions consécutives du script
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.settimeout(0)

    #Le socket est paramétré pour écouter sur toutes les interfaces réseau (''), sur le port 8888.
    #Pour modifier adresse et port, remplacer ici et dans le fichier client_poke_socket
    serversocket.bind(('', 8888))

    # lancer l'écouteur du socket serveur
    serversocket.listen()


    # on accepte des connexions jusqu'à avoir 2 joueurs
    print("En attente des joueurs...")
    while len(JOUEURS_LIST) < 2:

        connect=0
        while connect == 0 :
            #on tente d'accepter une connexion
            try:
                (clientsocket, address) = serversocket.accept()
                connect = 1
            except:
                sleep(1)

        connection_msg="Un nouveau combattant approche... => "+str(address)
        print(connection_msg)
        #envoi du message d'accueil au client
        clientsocket.send(connection_msg.encode('utf-8'))
        #réception du nom du joueur depuis le client
        nom_bin = clientsocket.recv(1024) 
        nom = nom_bin.decode('utf-8')
        #ajout des infos joueurs à JOUEURS_LIST, qui sera retourné par la fonction
        JOUEURS_LIST.append((clientsocket,nom))

    welcome_msg="Tous les joueurs sont connectés, la partie peut commencer !\n"
    print(welcome_msg)
    for i in range(len(JOUEURS_LIST)):
        JOUEURS_LIST[i][0].send(welcome_msg.encode('utf-8'))

    #on retourne le socket serveur et les infos joueurs pour que le script puisse les utiliser
    return(serversocket, JOUEURS_LIST)



#######################
#permet d'envoyer un message à un joueur
def send_message(socket,msg) :
    #sleep(0.5)
    socket.send(msg.encode('utf-8'))

#permet d'envoyer un message à tout les joueurs
def broadcast_message(sockets,msg) :
    for socket in sockets:
        socket.send(msg.encode('utf-8'))

'''
permet de recevoir un message d'un joueur.
pas encore implémenté dans le script principal
problèmes à régler : - dysfonctionnements dans la réception et l'envoi de messages dans le script client
                     - créer un système pour signaler au script client quand il doit écouter et envoyer
'''
def receive_message(socket) :
    msg=socket.recv(1024)
    msg_utf=msg.decode('utf-8')
    return msg_utf


#fonction de fermeture de tout les sockets
def close_server_socket(sockets,serversocket):
    for socket in sockets:
        socket.close()
    serversocket.close()
