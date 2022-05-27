###--------------------------------
# Importation des modules
###--------------------------------

# import bdd partie 2
import json
import csv
import random
import re













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
            self.crea_joueur(nom) #Lancement de la fonction de création d'un joueur
        self.nom=nom
        print("joueur",self.num, self.nom)
    
    def nbr_poke_joueur(self, nom):
        with open('bdd_joueurs.csv', 'r') as f:
            data_joueur = csv.DictReader(f)        
            for line in data_joueur:
                if line['name'] == nom:
                    nbr_pk=line['nbr_poke']
        self.nbr_poke=nbr_pk
        print("nombre de pokemon ",self.nbr_poke)
    
    # def id_poke_joueur(self,nom):
    #     with open('bdd_joueurs.csv', 'r') as f:
    #         data_joueur = csv.DictReader(f)        
    #         for line in data_joueur:
    #             if line['name'] == nom:
    #                 liste_pk=line['liste_poke']
    #     self.liste_poke=liste_pk
    #     print("liste pokemon ", self.liste_poke)
    #     return self.liste_poke

nom="joueur1"
with open('bdd_joueurs.csv', 'r') as f:
    data_joueur = csv.DictReader(f)        
    for line in data_joueur:
        if line['name'] == nom:
            pk_joueur=line['liste_poke']
print(pk_joueur)
w=pk_joueur[1:-1]
y=w.split(",")
print(y[0])

    ### Fonction pour créer un nouveau joueur + modification sur bdd.csv
    def crea_joueur(self,name):
        pok_1=random.randrange(0, 809) #Choix aléatoir des trois pokemon de démarage
        pok_2=random.randrange(0, 809)
        pok_3=random.randrange(0, 809)
        with open('bdd_joueurs.csv', 'a') as joueur_liste: #Rajoute du nouvel user sur la bdd
            write = csv.writer(joueur_liste)
            write.writerow([name,"3",[pok_1,pok_2,pok_3]])


class pokemon():
    # def __init__(self,nom):
    #     self.nom=nom
    #     self.status="ok"
    def __init__(self,id,nom,type,status,actif,faiblesse,resistance,hp,attaque,defense,sp_attaque,sp_def,vitesse):
        # self.id=0
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
        self.id=id
        self.nom=nom
        self.type=type
        self.status=status
        self.actif=actif
        self.faiblesse=faiblesse
        self.resistance=resistance
        self.hp=hp
        self.attaque=attaque
        self.defense=defense
        self.sp_attaque=sp_attaque
        self.sp_def=sp_def
        self.vitesse=vitesse
    def presentation_pokemon(self,joueur,id):
        self.id=id
        print("id",self.id,"nom",self.nom,"type",self.type,"status",self.status,"actif",self.actif,"faiblesse",self.faiblesse,"resistance",self.resistance,"hp",self.hp,"attaque",self.attaque,"defense",self.defense,"sp_attaque",self.sp_attaque,"sp_def",self.sp_def,"vitesse",self.vitesse)
    # def pokedex(self,id):
    #     data_pokemon= open("pokedex.json","r") 
    #     pokemonContent = data_pokemon.read()
    #     obj_pokemon = json.loads(pokemonContent)
    #     # obj_pokemon[0]['name']
    #     self.nom=obj_pokemon[1]['name']['french']


class action():
    def __init__(self):
        damage_multiplier = 1
    def attaque(self):
        pass
        # pour resistance et faiblesse            
        #   check type pok j1 et pok j2 
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
# Initiation des fonctions
###--------------------------------




###--------------------------------
# Lancement de la partie
###--------------------------------

pok1=pokemon(1,"pikachu","electric","ok",False,["herbe","dragon"],["eau","vol"],35,55,40,50,50,90)
pok2=pokemon(2,"salameche","feu","ok",False,["feu","dragon"],["eau","vol"],45,35,60,20,30,60)
pok3=pokemon(3,"carapuce","feu","ok",False,["combat","dragon"],["electric","vol"],55,40,30,40,20,50)
pok4=pokemon(4,"herbizare","herbe","ok",False,["electric","dragon"],["feu","vol"],15,75,30,45,65,80)


# 2 types de synthaxe
# pokemon.presentation_pokemon(pok1)
pok1.presentation_pokemon("joueur1",5)
# pok2.presentation_pokemon("joueur1",5)




### Récupération du nom d'user + création joueur via classe + Vérification sur bbd.csv

user_name=input("Joueur 1 quel est votre pseudo? ")
joueur_1=joueur(1)
joueur_1.presentation_joueur(user_name)



# liste_poke=joueur_1.id_poke_joueur(user_name)
# nbr=re.compile("[0-9]")
# z=list(filter(nbr.match, liste_poke))
# print(z)



nom="joueur1"
with open('bdd_joueurs.csv', 'r') as f:
    data_joueur = csv.DictReader(f)        
    for line in data_joueur:
        if line['name'] == nom:
            pk_joueur=line['liste_poke']
print(pk_joueur)
w=pk_joueur[1:-1]
y=w.split(",")
print(y[0])


# print(type(z))
# print(type(z[0]))
# for i in range(len(z)) :
#     print("z[i]",z[i])
#     print(i)
#     pokemon.presentation_pokemon(pok1,user_name,i+1)
# pok3.presentation_pokemon(user_name,z)


# user_name=input("Joueur 2 quel est votre pseudo? ")
# joueur_2=joueur(2)
# joueur_2.presentation_joueur(user_name)







### /!\ verifs:
# Si pokemons à vitesse égale pour le départ
# Pokemon en double dans la liste des pokes du joueur
# => soit id pokemons pour avoir doublons
# => soit un pokemon de chaque



