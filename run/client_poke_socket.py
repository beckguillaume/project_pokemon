## pokemon_socket ##
####################
###### CLIENT ######


'''
client_poke_socket est le script des joueurs qui se connectent 
et interragissent avec le script principal dans le dossier run.

Ce fichier a été fortement appauvri du fait de dysfonctionnements 
lors de la réception et l'émission de messages.

Plus de recherches sont nécessaires pour arriver à une version finale.

en l'état, les clients peuvent se connecter au script, envoyer 
leur nom de joueur et recevoir les messages d'initialisation de la partie
'''

import socket

#informations à modifier en fonction de l'adresse et du port d'écoute du serveur
#si non modifié, le serveur écoute sur localhost:8888
HOST = "127.0.0.1" #adresse serveur
PORT = 8888 # Port en écoute

# création d'un socket en IPv4
print("création du socket en cours...\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# on se connecte à une IP et un port en écoute
print("connexion...\n")
s.connect((HOST, PORT))

# Réception du message de connexion du serveur
data=s.recv(1024)
print(data.decode('utf-8'))

#Envoi du nom du joueur
msg=input("Quel est ton nom, jeune dresseur ? ")
s.sendall(msg.encode('utf-8'))

# Réception du message d'accueil du serveur
data=s.recv(1024)
print(data.decode('utf-8'))


# non fonctionnel avec une boucle While
data=s.recv(1024)
print(data.decode('utf-8'))

data=s.recv(1024)
print(data.decode('utf-8'))

data=s.recv(1024)
print(data.decode('utf-8'))


# closing socket
s.close()
