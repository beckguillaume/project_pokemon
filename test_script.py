###--------------------------------
# Importation des modules
###--------------------------------
import json
import csv
import random



###--------------------------------
# Initiation des fonctions
###--------------------------------

### Fonction pour créer un nouveau joueur + modification sur bdd.csv
def crea_joueur(name):
    pok_1=random.randrange(0, 809) #Choix aléatoir des trois pokemon de démarage
    pok_2=random.randrange(0, 809)
    pok_3=random.randrange(0, 809)
    with open('bdd_joueurs.csv', 'a') as joueur_liste: #Rajoute du nouvel user sur la bdd
        write = csv.writer(joueur_liste)
        write.writerow([name,"3",[pok_1,pok_2,pok_3]])







###--------------------------------
# Initiation des classes
###--------------------------------


class joueur():
    def __init__(self,num):
        self.num=num
    
    def presentation_joueur(self, nom):
        pseudo_ok=False
        with open('bdd_joueurs.csv', 'r') as f:
            data_joueur = csv.DictReader(f)        
            for line in data_joueur: 
                pseudo=line['name']
                if nom in pseudo:
                    pseudo_ok=True
        #Création de l'user si pseudo absent (=False)            
        if pseudo_ok == True: 
            print("Bienvenu")       
        else:
            print("Nous allons créer votre joueur")
            crea_joueur(nom) #Lancement de la fonction de création d'un joueur
        self.nom=nom
        print("joueur",self.num, self.nom)
    def nbr_poke_in_game(self, nom):
        with open('bdd_joueurs.csv', 'r') as f:
            data_joueur = csv.DictReader(f)        
            for line in data_joueur:
                if line['name'] == nom:
                    nbr_pk=line['nbr_poke']
        self.nbr_poke=nbr_pk
        print("nombre de pokemon ",self.nbr_poke)




class pokemon():
    def __init__(self,nom):
        self.nom=nom
        self.status="ok"
#   def __init__(self,nom,type,status,actif,faiblesse,resistance,hp,attaque,defense,sp_attauqe,sp_def,vitesse):
        # self.nom=pikachu
        # self.type=electric
        # self.status=ok
        # self.actif=False
        # self.faiblesse=[herbe,dragon]
        # self.resistance=[eau,vol]
        # self.hp=35
        # self.attaque=55
        # self.defense=40
        # self.sp_attaque=50
        # self.sp_def=50
        # self.vitesse=90
    def presentation_pokemon(self):
        print("nom",self.nom)

pok1=pokemon("pikachu")

# 2 types de synthaxe
pokemon.presentation_pokemon(pok1)
pok1.presentation_pokemon()



class action():
    def __init__(self):
        damage_multiplier = 1
        def attaque(self):
            pass
            # check type pok j1 et pok j2 
            # pour resistance et faiblesse
            # attaque - def --> if > 0 : enleve pv
            
        def change(self):
            pass
            # appelle collection_pokemon pour afficher les pokemons du joueur
            # choisi un pokemon (input user) nom du pokemon (attention doublon)
            # pokemon choisi devient actif et l'ancien inactif
        def collection_pokemon(self):
            pass
            # affiche la liste des pokemons du joueur
            # utiliser presentation_joueur et presentation_pokemon ?
            # fonciton utile ou non ?
        def fuite(self):
            pass
            # 1/4 chance de fuite
            # si réussite, appelle partie.fin_partie
            # sinon passe le tour à l'autre joueur

class partie():
    def __init__(self):
        pass
    def fin_partie():
        pass
        # tout les pokemons ko
        # ou un joueur fuit
    def debut():
        pass
        # choisi 2 joueurs
        # restore hp et change status de ko > ok
        # pick random pokemon dans le roester (random sur range nombre pokemon)
        # check vitesse des 2 pokemons
        # coinflip si vitesse égale







###--------------------------------
# Lancement de la partie
###--------------------------------


### Récupération du nom d'user + création joueur via classe + Vérification sur bbd.csv

user_name=input("Joueur 1 quel est votre pseudo? ")
joueur_1=joueur(1)
print(joueur_1.presentation_joueur(user_name))

user_name=input("Joueur 2 quel est votre pseudo? ")
joueur_2=joueur(2)
print(joueur_2.presentation_joueur(user_name))
print(joueur_2.nbr_poke_in_game(user_name))







### /!\ verifs:
# Si pokemons à vitesse égale pour le départ
# Pokemon en double dans la liste des pokes du joueur



