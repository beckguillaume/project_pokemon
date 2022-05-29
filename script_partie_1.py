# --------------------------------
# Importation des modules
# --------------------------------

import random

##import bdd format dico

dic_joueur = [{"joueur": "gertrude",
                "ls_poke": [{
                "id": 4,
                "status": "inactif",
                "name": {
                    "english": "Charmander",
                    "japanese": "ヒトカゲ",
                    "chinese": "小火龙",
                    "french": "Salamèche"
                },
                "type": [
                    "Fire"
                ],
                "base": {
                    "HP": 39,
                    "Attack": 52,
                    "Defense": 43,
                    "Sp. Attack": 60,
                    "Sp. Defense": 50,
                    "Speed": 65
                }
                },
                {
                "id": 756,
                "status": "inactif",
                "name": {
                    "english": "Shiinotic",
                    "japanese": "マシェード",
                    "chinese": "灯罩夜菇",
                    "french": "Lampignon"
                },
                "type": [
                    "Grass",
                    "Fairy"
                ],
                "base": {
                    "HP": 60,
                    "Attack": 45,
                    "Defense": 80,
                    "Sp. Attack": 90,
                    "Sp. Defense": 100,
                    "Speed": 30
                }
                },
                {
                "id": 5,
                "status": "inactif",
                "name": {
                    "english": "Charmeleon",
                    "japanese": "リザード",
                    "chinese": "火恐龙",
                    "french": "Reptincel"
                },
                "type": [
                    "Fire"
                ],
                "base": {
                    "HP": 58,
                    "Attack": 64,
                    "Defense": 58,
                    "Sp. Attack": 80,
                    "Sp. Defense": 65,
                    "Speed": 80
                }
                }]
                },
                {
                "joueur": "albert",
                "ls_poke": [{
                    "id": 102,
                    "status": "inactif",
                    "name": {
                        "english": "Exeggcute",
                        "japanese": "タマタマ",
                        "chinese": "蛋蛋",
                        "french": "Noeunoeuf"
                    },
                    "type": [
                        "Grass",
                        "Psychic"
                    ],
                    "base": {
                        "HP": 60,
                        "Attack": 40,
                        "Defense": 80,
                        "Sp. Attack": 60,
                        "Sp. Defense": 45,
                        "Speed": 40
                    }
                    },
                    {
                    "id": 103,
                    "status": "inactif",
                    "name": {
                        "english": "Exeggutor",
                        "japanese": "ナッシー",
                        "chinese": "椰蛋树",
                        "french": "Noadkoko"
                    },
                    "type": [
                        "Grass",
                        "Psychic"
                    ],
                    "base": {
                        "HP": 95,
                        "Attack": 95,
                        "Defense": 85,
                        "Sp. Attack": 125,
                        "Sp. Defense": 75,
                        "Speed": 55
                    }
                    } ]
                }]


# -------------------------------------------
# Initation des fonctions et classes
# -------------------------------------------


###Fonction pour récupérer nom du joueur + check si présent bdd
def start():
    pokemaster=[]
    dresseur=0
    while dresseur < 2:
        user=input("Quel est votre nom? ")
        #bdd search joueur
        creation=True
        i=0
        while i < len(dic_joueur): #a adapter en fonction de la bdd
            if dic_joueur[i]["joueur"] == user:
                print(user, "joueur existant")
                creation=False
                dresseur+=1
                pokemaster.append(user)
            i+=1
        if creation==True:
            print(user, "A créer")
            dresseur+=1
            pokemaster.append(user)
    #print(pokemaster)
            #bdd create add.joueur
    return pokemaster



### class pour fonctions d'initalisation de la partie
class qui_commence():
    
    ## Fonction activation aléatoire d'un pokemon par joueur pour début du jeu
    def activation_poke (self,pokemaster): 
        for i in range(len(pokemaster)):
            for j in range(len(dic_joueur)):
                if pokemaster[i] == dic_joueur[j]["joueur"]:
                    ls_poke=dic_joueur[j]["ls_poke"]
                    nbr_poke=len(ls_poke)
                    num=random.randint(0, nbr_poke-1)
                    dic_joueur[j]["ls_poke"][num]["status"]="actif"     
 
    ## Fonction pour avoir joueur + son pokemon actif               
    def tab_jeu(self, pokemaster): 
        tab_jeu=[]
        # self.tab_jeu=tab_jeu
        for i in range(len(pokemaster)):
            joueur_name=[]
            for j in range(len(dic_joueur)):
                ls_poke=dic_joueur[j]["ls_poke"]
                if pokemaster[i] == dic_joueur[j]["joueur"]:
                    for p in range(len(ls_poke)):
                        if dic_joueur[j]["ls_poke"][p]["status"] == "actif":
                            poke=dic_joueur[j]["ls_poke"][p]["name"]["french"]
                            joueur_name.append(pokemaster[i])
                            joueur_name.append(poke)
                            tab_jeu.append(joueur_name)
                            #print(tab_jeu)
        return tab_jeu
    
    ## Fonction pour choix de qui sera joueur1 ou joueur2 pour la partie // joueur_1=nom du joueur 1 + nom de son pok actif                      
    def choix_poke_depart(self, pokemaster): 
        #Récupération de la vitesse des poke choisi aléatoirement précedement
        vitesse=[]
        for i in range(len(pokemaster)):
            joueur_name=[]
            for j in range(len(dic_joueur)):
                ls_poke=dic_joueur[j]["ls_poke"]
                if pokemaster[i] == dic_joueur[j]["joueur"]:
                    for p in range(len(ls_poke)):
                        if dic_joueur[j]["ls_poke"][p]["status"] == "actif":
                            poke=dic_joueur[j]["ls_poke"][p]["name"]["french"]
                            joueur_name.append(pokemaster[i])
                            joueur_name.append(poke)
                            v=dic_joueur[j]["ls_poke"][p]["base"]["Speed"]
                            joueur_name.append(v)
                            vitesse.append(joueur_name)  
        #Ordre de passage des joueurs en fonction du pokemon le plus rapide + choix aléatoire si égalité          
        if vitesse[0][2] < vitesse[1][2]:
            print("C'est",vitesse[1][0],"qui commence")
            #print(tab_jeu[0][2], tab_jeu[1][2])
            joueur_1=vitesse[1]
            joueur_2=vitesse[0]
        elif vitesse[0][2] > vitesse[1][2]:
            #print("cacahouette")
            print("C'est",vitesse[0][0],"qui commence")
            joueur_2=vitesse[1]
            joueur_1=vitesse[0]
        else:
            r=random.randint(0,1)
            if r == 0:
                print("C'est",vitesse[0][0],"qui commence")
                joueur_2=vitesse[1]
                joueur_1=vitesse[0]
            if r == 1:
                print("C'est",vitesse[1][0],"qui commence")
                joueur_1=vitesse[1]
                joueur_2=vitesse[0]
        #print(joueur_1, joueur_2)
        #suppresion de la valeur de la vitesse inutile pour le reste du jeu
        joueur_1.pop(-1)
        joueur_2.pop(-1)
        return joueur_1, joueur_2


###Fonction pour récupérer des informations sur le pokemon actif
def info_poke_actif(joueur):
    game_in = True
    info_poke={}
    for j in range(len(dic_joueur)):
        ls_poke=dic_joueur[j]["ls_poke"]
        if ls_poke == 0:
            game_in=False                       
        else:            
            for p in range(len(ls_poke)):
                if joueur[1] == dic_joueur[j]["ls_poke"][p]["name"]["french"]:
                    info_poke=dic_joueur[j]["ls_poke"][p]["base"]
                    print("Voici les statistiques de votre pokemon",joueur[1],":")
                    #print(info_poke)
    return info_poke, game_in


###Fonction pour présenter les joueurs
def presentation_joueur(joueur_1, joueur_2):
    print("Joueur_1:", joueur_1)
    print("joueur_2 :", joueur_2)

###classe actions avec menu de jeu + actions

class actions():
       
    def poke_changement_proprio(self, a, b):
        #récupération des infos du poke que le joueur b a perdu
        for i in range(len(dic_joueur)):             
            if b[0] == dic_joueur[i]["joueur"]:
                ls_poke=dic_joueur[i]["ls_poke"]          
                for p in range(len(ls_poke)):  
                    print(b[1])              
                    if b[1] == dic_joueur[i]["ls_poke"][p]["name"]["french"]:
                        dic_joueur[i]["ls_poke"][p]["status"]="inactif"
                        num_pok=p
                        copie = dic_joueur[i]["ls_poke"][num_pok]                        
                        del dic_joueur[i]["ls_poke"][p] 
                        break                       
                        # num_poke=p
                        # num_joueur=i
        #supression du poke dans la liste du joueur b  
        #if game_in == True:           
        #del dic_joueur[num_joueur]["ls_poke"][num_poke]
        #ajout du poke dans la liste du joueur a          
        for i in range(len(dic_joueur)):
            if a[0] == dic_joueur[i]["joueur"]:
                dic_joueur[i]["ls_poke"].append(copie)
        
        game_in=True        
        for i in range(len(dic_joueur)):
            if a[0] == dic_joueur[i]["joueur"]:
                ls_poke=int(len(dic_joueur[i]["ls_poke"]))
                if ls_poke == 0:
                    game_in=False 
                else:
                    c=0
                    for p in range(ls_poke):              
                        if dic_joueur[i]["ls_poke"][p]["base"]["HP"] >0:
                            c+=1
                    if c == 0:
                        game_in=False
            if b[0] == dic_joueur[i]["joueur"]:
                ls_poke=int(len(dic_joueur[i]["ls_poke"]))
                if ls_poke == 0:
                    game_in=False 
                else:
                    c=0
                    for p in range(ls_poke):              
                        if dic_joueur[i]["ls_poke"][p]["base"]["HP"] > 0:
                            c+=1
                    if c == 0:
                        game_in=False
                
        #print(dic_joueur)
        return game_in
    
                
    ## Fonction pour l'option attaque avec a = joueur qui attaque et b joueur qui subit        
    def attaque(self, a, b): 
        game_in=True
        perte_poke=False
        (info_poke_1, game_in)=info_poke_actif(a)
        print(info_poke_1)
        att_pk1 = info_poke_1["Attack"]
        (info_poke_2, game_in)=info_poke_actif(b)
        print(info_poke_2)
        def_pk2 = info_poke_2["Defense"]
        hp_pk2=info_poke_2["HP"]
        #check type bdd pour faiblesses et résistances
        damage_multiplier = 3
                # pour resistance et faiblesse
                #   check type pok j1 et pok j2
                # attaque - def --> if > 0 : enleve pv
                #print(att_pk1, def_pk2, hp_pk2)
        
        #print(a[1],"attaque")
        print("\033[0;31m" + a[1] +" attaque" + "\033[0m")
        
        degats = att_pk1 * damage_multiplier - def_pk2
        #print(def_pk2, att_pk1)
        #print(degats)
        if degats > 0:
            hp_pk2 = hp_pk2 - degats        
        if hp_pk2 <= 0:
            perte_poke=True
            #print(b[1], "KO")
            print("\033[0;31m" + b[1], " KO" + "\033[0m")
            #print(b[1], "change de dresseur")
            print("\033[0;31m" + b[1], " change de dresseur"+ "\033[0m")
            for j in range(len(dic_joueur)):
                ls_poke=dic_joueur[j]["ls_poke"]
                for p in range(len(ls_poke)):
                    if b[1] == dic_joueur[j]["ls_poke"][p]["name"]["french"]:
                        dic_joueur[j]["ls_poke"][p]["base"]["HP"] = 0
            
            game_in=self.poke_changement_proprio(a, b)
            #si nbr_poke=0 pas de changement de pokemon
            if game_in == True:
                (game_in)=self.changement_de_pokemon(b)
            
            #info_poke_2["HP"]=0
        else: info_poke_2["HP"]=hp_pk2
        #print(hp_pk2)
        return game_in, perte_poke
    
    ## Fonction pour l'option fuite
    def fuite(self): 
        game_in=True
        n=random.randint(0, 4)
        result_fuite=False
        if n == 4:
            #print("Fuite réussie") # == fin du jeu + enregistrement des infos
            result_fuite=True
            game_in=False        
        else:
            #print("Fuite echouée") # == tour au joueur suivant
            result_fuite=False
        return result_fuite, game_in
            
    ## Fonction pour l'option changement de pokemon + dans option attaque si pokemon KO
    def changement_de_pokemon(self, a):
        game_in=True        
        liste_poke_dispo=[]   
        for j in range(len(dic_joueur)):
            ls_poke=dic_joueur[j]["ls_poke"]
            if len(ls_poke) == 0:
                game_in=False
            else:
                if a[0] == dic_joueur[j]["joueur"]:
                    for p in range(len(ls_poke)):
                        if dic_joueur[j]["ls_poke"][p]["status"] == "inactif" and dic_joueur[j]["ls_poke"][p]["base"]["HP"] > 0 :
                            poke=dic_joueur[j]["ls_poke"][p]["name"]["french"]
                            liste_poke_dispo.append(poke)
        if game_in==True:                    
            print("vous pouvez appeler :")                    
            for i in range(len(liste_poke_dispo)):
                print(i,liste_poke_dispo[i])

            choix_poke=int(input("Choisissez votre pokemon par le numéro: "))
            #passage des actif en inactif
            #print(dic_joueur)
            for j in range(len(dic_joueur)):
                ls_poke=dic_joueur[j]["ls_poke"]
                if a[0] == dic_joueur[j]["joueur"]:
                    for p in range(len(ls_poke)):
                        if dic_joueur[j]["ls_poke"][p]["status"] == "actif":
                            dic_joueur[j]["ls_poke"][p]["status"] = "inactif"
                        if dic_joueur[j]["ls_poke"][p]["name"]["french"] == liste_poke_dispo[choix_poke]:
                            dic_joueur[j]["ls_poke"][p]["status"] = "actif"
                            a[1]=dic_joueur[j]["ls_poke"][p]["name"]["french"]
                            print(a)
            #passage du poke choisi d'inactif a actif
            # for j in range(len(dic_joueur)):
            #     ls_poke=dic_joueur[j]["ls_poke"]
            #     if a[0] == dic_joueur[j]["joueur"]:
            #         for p in range(len(ls_poke)):
                        
                        print("pokemon changé")
                        info_poke_actif(a)
            #print(dic_joueur)
        elif game_in==False:
            print("Vous n'avez plus de pokemon")
        return game_in
    
    ## Fonction affichage menu d'action + lancement action avec input
    def menu_jeu(self, a, b): 
        game_in=True  
        perte_poke=False           
        print("1 : attaquer")
        print("2 : changer de pokemon")
        print("3 : tenter de fuire")
        choix_menu=int(input("Que souhaitez-vous faire ? "))
        if choix_menu == 1:
            #print("attaque")
            (game_in, perte_poke)=self.attaque(a, b)         
        elif choix_menu == 2:
            #print("changement")
            (game_in)=self.changement_de_pokemon(a)         
        elif choix_menu == 3:
            #print("fuite")
            (result_fuite, game_in)=self.fuite()
            if result_fuite == True:
                #print("Fuite réussie")
                print("\033[0;32m" + "Fuite réussie" + "\033[0m")
                #print(a[0],"s'est enfui")
                print("\033[0;32m"+ a[0]," s'est enfui" + "\033[0m") 
                game_in = False # = fin du jeu
            elif result_fuite == False:
                #print("Fuite échouée")
                print("\033[0;31m"+ "Fuite échouée" + "\033[0m") 
        return game_in, perte_poke


                 



# # --------------------------------
# # Lancement de la partie
# # --------------------------------


(pokemaster)=start()
print("start")

initialisation=qui_commence()
initialisation.activation_poke(pokemaster)

(tab_jeu)=initialisation.tab_jeu(pokemaster)


(joueur_1, joueur_2)=initialisation.choix_poke_depart(pokemaster)


##Récupération du nombre de pokemon par joueur + 
#def recup_nbr_poke(joueur_1, joueur_2):
for y in range(len(dic_joueur)):
    if joueur_1[0] == dic_joueur[y]["joueur"]:
        #id_joueur_1=y
        nbr_poke_1=len(dic_joueur[y]["ls_poke"])
for z in range(len(dic_joueur)):
    if joueur_2[0] == dic_joueur[z]["joueur"]:
        #id_joueur_1=z
        nbr_poke_2=len(dic_joueur[z]["ls_poke"])
#return nbr_poke_1, nbr_poke_2    




game=actions()
game_in=True
while nbr_poke_2 > 0 and nbr_poke_1 > 0 and game_in == True:
    again="on"        
    while again == "on" and nbr_poke_1 > 0 and game_in == True:
        print("C'est au tour de", joueur_1[0])
        #info_poke_actif(joueur_1)
        #print("game en cours")
        (game_in, perte_poke)=game.menu_jeu(joueur_1, joueur_2)
        if perte_poke == True:
            nbr_poke_1-=1
        #print(game_in)
        #print(dic_joueur)
        again="off"
        
    again="on"
    while again == "on" and nbr_poke_2 > 0 and game_in == True:
        print("C'est au tour de", joueur_2[0])
        #info_poke_actif(joueur_2)
        #print("game en cours")
        (game_in, perte_poke)=game.menu_jeu(joueur_2, joueur_1)
        if perte_poke == True:
            nbr_poke_2-=1
        #print(game_in)
        #print(dic_joueur)
        again="off"

if nbr_poke_2 > 0 and nbr_poke_1 == 0:
    print("Bravo", joueur_2[0])
    print("\033[0;36m" + "Bravo", joueur_2[0] + "\033[0m")
elif nbr_poke_2 == 0 and nbr_poke_1 > 0:
    print("Bravo", joueur_1[0])
    print("\033[0;36m" + "Bravo", joueur_1[0] + "\033[0m")


# # --------------------------------
# # Fin de script
# # --------------------------------



