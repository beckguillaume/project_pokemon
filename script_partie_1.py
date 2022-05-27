import random

dic_joueur_1 = { "joueur": "gertrude",
                "ls_poke": [{
                "id": 4,
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
                }

dic_joueur_2 = { "joueur": "Albert",
                "ls_poke": [{
                "id": 4,
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
                "id": 5,
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
                }



#2 joueurs
#random de poke


#fonction start
#fonction présentation joueur
#fonction présentation poke
#fonction menu attaque change fuite
#fonction win

def win():
    for j in liste_joueur:
        nbr_poke=len(j["ls_poke"])
        if nbr_poke == 0: #ou si joueur fuite
            print("Joueur",j,"lose")
            return True
        return False

def partie():
    j=0
    while win() != True:
        print("game en cour")
        #appel fonction attaque etc
        j+=1
        if j == 2:
            j=0
        
   

def start():
    pokemaster=[]
    dresseur=0
    while dresseur < 2:        
        user=input("Quel est votre nom? ")
        #bdd search joueur
        creation=True
        i=0
        while i < len(liste_joueur): #a adapter en fonction de la bdd
            if liste_joueur[i]["joueur"] == user: 
                print("joueur existant", dresseur+1, user)
                creation=False
                dresseur+=1
                pokemaster.append(user)
            i+=1  
        if creation==True:
            print("A créer", dresseur+1, user)
            dresseur+=1
            pokemaster.append(user)
    print(pokemaster)
            #bdd create add.joueur 
    return pokemaster 

def qui_commence(pokemaster, liste_joueur):
    poke_nom=[]
    for i in range(len(pokemaster)):
        joueur_name=[]
        for j in range(len(liste_joueur)):
            if pokemaster[i] == liste_joueur[j]["joueur"]:
                ls_poke=liste_joueur[j]["ls_poke"]
                nbr_poke=len(ls_poke)
                poke_numero=random.randint(0, nbr_poke-1)
                # print(nbr_poke)
                # print("match",i ,j, pokemaster[i], liste_joueur[j]["joueur"])  
                # print(liste_joueur[j]["ls_poke"][poke_numero]["name"]["french"])
                n=liste_joueur[j]["ls_poke"][poke_numero]["name"]["french"]
                v=liste_joueur[j]["ls_poke"][poke_numero]["base"]["Speed"]     
                joueur_name.append(pokemaster[i])
                joueur_name.append(n) 
                joueur_name.append(v)                
                poke_nom.append(joueur_name) 
    
    if poke_nom[0][2] < poke_nom[1][2]:
        print("C'est",poke_nom[1][0],"commence")
        #print(poke_nom[0][2], poke_nom[1][2])
        joueur_1=poke_nom[1]
        joueur_2=poke_nom[0]        
    elif poke_nom[0][2] > poke_nom[1][2]:
        #print("cacahouette")
        print("C'est",poke_nom[0][0],"commence")
        joueur_2=poke_nom[1]
        joueur_1=poke_nom[0]
    else: 
        r=random.randint(0,1)
        if r == 0:
            print("C'est",poke_nom[0][0],"commence")
            joueur_2=poke_nom[1]
            joueur_1=poke_nom[0]
        if r == 1:
            print("C'est",poke_nom[1][0],"commence")
            joueur_1=poke_nom[1]
            joueur_2=poke_nom[0] 
    #print(joueur_1, joueur_2)            
                
    return poke_nom, joueur_1, joueur_2              
                
                




       
def presentation_joueur(pokemaster):
    joueur_1=pokemaster[0]
    joueur_2=pokemaster[1]   
    
    
    
    
    
liste_joueur=[dic_joueur_1, dic_joueur_2]
#partie() 
pokemaster=start()
(poke_nom, joueur_1, joueur_2)=qui_commence(pokemaster, liste_joueur)
print(joueur_1, joueur_2)
print(poke_nom)





# print(dic_joueur_1["joueur"])
# print(dic_joueur_2["joueur"])