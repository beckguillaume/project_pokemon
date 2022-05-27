import random
# import bdd from script_bdd.py

class joueur():
    def __init__(self,nom,pokemon):
        self.nom=nom
        self.nbre_pokemon=0
        self.liste_pokemon=pokemon
    def presentation_joueur(self):
        print("nom",self.nom)
        print("pokemon :",self.pokemon)


class pokemon():
    def __init__(self):
        self.chiotte="pouet"
        #pass
        # self.nom=nom
        # self.status="ok"
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
    def presentation_pokemon(self, numero):
        self.name=dic_joueur_1["ls_poke"][numero]["name"]["french"]
        print("nom",self.name)
    def random(self):
        nbr_poke=len(dic_joueur_1["ls_poke"])
        numero=random.randint(0, nbr_poke)
        print(numero)





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
    def debut(self):

        pass
        # choisi 2 joueurs
        # restore hp et change status de ko > ok
        # pick random pokemon dans le roester (random sur range nombre pokemon)
        # check vitesse des 2 pokemons
        # coinflip si vitesse égale

# tout pokemon mort > retire le joueur

# pokemon ko > recuperer par l'adversaire (etat ko pour ce combat)












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

print(dic_joueur_1["joueur"])
print(dic_joueur_2["joueur"])

# joueur1=(dic_joueurs["joueur"])
# print(dic_joueurs["ls_poke"][0]["id"])
# nbr_poke=len(dic_joueur_1["ls_poke"])
# print(nbr_poke)

pokemon.random()