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
    
    def id_poke_joueur(self,nom):
        # nom="joueur1"
        with open('bdd_joueurs.csv', 'r') as f:
            data_joueur = csv.DictReader(f)        
            for line in data_joueur:
                if line['name'] == nom:
                    pk_joueur=line['liste_poke']
        # print(pk_joueur)
        w=pk_joueur[1:-1]
        y=w.split(",")
        return y
        # print(y[0])

    ### Fonction pour créer un nouveau joueur + modification sur bdd.csv
    def crea_joueur(self,name):
        pok_1=random.randrange(0, 809) #Choix aléatoir des trois pokemon de démarage
        pok_2=random.randrange(0, 809)
        pok_3=random.randrange(0, 809)
        with open('bdd_joueurs.csv', 'a') as joueur_liste: #Rajoute du nouvel user sur la bdd
            write = csv.writer(joueur_liste)
            write.writerow([name,"3",[pok_1,pok_2,pok_3]])


class pokemon():
    def __init__(self,id,nom,type,status,actif,faiblesse,resistance,hp,attaque,defense,sp_attaque,sp_def,vitesse):
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
    def presentation_pokemon(self):
        #self.id=id
        print("id",self.id,"nom",self.nom,"type",self.type,"status",self.status,"actif",self.actif,"faiblesse",self.faiblesse,"resistance",self.resistance,"hp",self.hp,"attaque",self.attaque,"defense",self.defense,"sp_attaque",self.sp_attaque,"sp_def",self.sp_def,"vitesse",self.vitesse)
    # def pokedex(self,id):
    #     data_pokemon= open("pokedex.json","r") 
    #     pokemonContent = data_pokemon.read()
    #     obj_pokemon = json.loads(pokemonContent)
    #     # obj_pokemon[0]['name']
    #     self.nom=obj_pokemon[1]['name']['french']






class action():
    def __init__(self, pok1, pok2):
        self.damage_multiplier = 1
        self.att_pk1=pok1.attaque
        self.def_pk2=pok2.defense
        self.hp_pk2= pok2.hp

    def attaque(self):
        print("Pok1 attaque")
        # pour resistance et faiblesse            
        #   check type pok j1 et pok j2 
        # attaque - def --> if > 0 : enleve pv
        print(self.hp_pk2)
        degats = self.def_pk2 - self.att_pk1 
        self.hp_pk2-= degats
        print(self.hp_pk2)
        if self.hp_pk2 <= 0 :
            print("pok2 KO")
            pass
            # actualiser le status du pokemon 2 en ko
            # call module change pour joueur 2
            # vérif vie max pour bdd
        else :
            print ("continuer a vous taper dessus")
        # interrupteur change joueur

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
    def __init__(self, numero):

        pass
    def debut(self, user_name):

        pass
        # tout les pokemons ko
        # ou un joueur fuit
    def liste_pk_joueurs(self, user_name):

        print(i)
            
            
        
    def fin_partie():
        pass
        # choisi 2 joueurs
        # restore hp et change status de ko > ok
        # pick random pokemon dans le roester (random sur range nombre pokemon)
        # check vitesse des 2 pokemons
        # coinflip si vitesse égale



###--------------------------------
# Lancement de la partie
###--------------------------------

pok1=pokemon(1,"pikachu","electric","ok",False,["herbe","dragon"],["eau","vol"],35,55,40,50,50,90)
pok2=pokemon(2,"salameche","feu","ok",False,["feu","dragon"],["eau","vol"],45,35,60,20,30,60)
pok3=pokemon(3,"carapuce","feu","ok",False,["combat","dragon"],["electric","vol"],55,40,30,40,20,50)
pok4=pokemon(4,"herbizare","herbe","ok",False,["electric","dragon"],["feu","vol"],15,75,30,45,65,80)

print(pok1.vitesse)

# joueur_1=partie(1).debut
# partie(2).debut
# joueur_1.liste_pk_joueurs()





action(pok1, pok2).attaque()
print(pok1.presentation_pokemon())
print(pok2.presentation_pokemon())





# 2 types de synthaxe
# pokemon.presentation_pokemon(pok1)
# pok1.presentation_pokemon(5)

### Récupération du nom d'user + création joueur via classe + Vérification sur bbd.csv



# liste_poke_j1=joueur_1.id_poke_joueur(user_name)
# print(liste_poke_j1)
# print(liste_poke_j1[0])

# for i in range(len(liste_poke_j1)):


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



