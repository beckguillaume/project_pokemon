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
print("création socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("set blocking")

# on se connecte à une IP et un port en écoute
print("connection")
s.connect((HOST, PORT)) 

print("on récupère les données..")
# receive data
data=s.recv(1024)

# print data
print(data.decode('utf-8')) # pour l'instant, obliger de faire "enter" pour afficher... on sait pas trop pq
print("n'importe quoi pour se repérer") # PB ne s'affiche pas dans le terminal client

# let's chat
while exit == 0 :
    msg=input("Entrez quelque chose svp")
    s.sendall(msg.encode('utf-8'))
    if data.decode('utf-8') == 'exit':
        exit=1
        
# closing socket
s.close()
