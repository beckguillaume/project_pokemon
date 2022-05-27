# pokemon_socket #################
##################################
##### CLIENT #####################
##################################
import socket

exit=0
HOST = "91.165.234.129" #adresse serveur chez Arthur
PORT = 8888 # Port en écoute

# création d'un socket en IPv4
#SOCK_STREAM : TCP, SOCK_DRGAM : UDP
print("création du socket en cours...\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# on se connecte à une IP et un port en écoute
print("connexion...\n")
s.connect((HOST, PORT))

print("connexion réussie !\n")

# Réception du message d'accueil du serveur
data=s.recv(1024)
print(data.decode('utf-8'))

#le serveur indique si on est joueur 1 ou 2
data=s.recv(1024)

if int(data) == 0 : # on est le joueur 1

    # let's chat
    while exit == 0 :
        msg=input("/> ")         # le joueur 1 envoie d'abord
        s.sendall(msg.encode('utf-8'))
        
        if msg.decode('utf-8') == 'exit':            # et exit s'il veut exit
            exit=1

        data=s.recv(1024)                             # puis écoute
        print(data.decode('utf-8'))
        
        if data.decode('utf-8') == 'exit':            # et exit s'il reçoit exit
            exit=1
            


else :  # on est le joueur 2
        # let's chat
    while exit == 0 :
        
        data=s.recv(1024)                           # le joueur 2 écoute d'abord
        print(data.decode('utf-8'))

        if data.decode('utf-8') == 'exit':          # et exit s'il reçoit exit
            exit=1
        else :
            msg=input("/> ")   # sinon il envoie
            s.sendall(msg.encode('utf-8'))
            if msg.decode('utf-8') == 'exit':          # et exit s'il reçoit exit
                exit=1
        
# closing socket
s.close()
