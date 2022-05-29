# pokemon_socket #################
##################################
##### CLIENT #####################
##################################
import socket

exit=0
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

data=s.recv(1024)
print(data.decode('utf-8'))

data=s.recv(1024)
print(data.decode('utf-8'))

data=s.recv(1024)
print(data.decode('utf-8'))


# closing socket
s.close()
