################# BDD POKEMON #####################
#                   Partie 2 
# Auteurs : Syndney et Félix

################## ATTENTION #######################
# La partie, donc les intéraction avec la BDD ne fonctionne pas, nous avons compris
# les différentes intéraction à effectuer avec la BDD et les fichiers json, mais
# nous n'avons pas réussis à manipuler et intéragit avec ces deux objets.
###################################################


# Importation des modules
import json
import random

#Définition de la classe BDD contenant 3 attributs associées aux 3 BDD : le pokedex total, les types, et les noms des joueurs avec leurs pokedex qu'ils possèdent 
class bdd():
    def __init__(self):
        # Chargement du pokedex de l'ensemble des pokemons
        with open("pokedex.json","r") as f :
            self.data_pokemon=json.load(f)

        # Le fichier joueurs.json est un dictionnaire contenant plusieurs clées :
        # Le nom du joueur, les pokemons de sa collection, et si le pokémon est ko ou non (actif ou non)
        with open("joueurs.json","r") as f :
            self.data_joueurs=json.load(f)

        # Chargement de l'ensemble des forces et faiblesses des types :
        with open("pokemon_type.json","r") as f :
            self.data_type=json.load(f)

    # Définition d'une méthode pour ajouter un joueur à la BDD joueurs :
    def add_joueur(self,input_joueur):   
        with open('joueurs.json','r+') as f :
            self.data_joueurs["nom"] = input_joueur

    # Définition de la méthode pour ajouter un pokemon aléatoire au joueur :
    def random_pokemon(self,input_joueur):
        pokemon=random.choice(self.data_pokemon)
            with open('joueurs.json','r+') as f :
            self.data_joueurs[input_nom_joueur]["pokemons"].append(pokemon)
    
    # Définition de la méthode pour retourner un nom de joueur et les pokemons de sa collection :
     def get_joueur(self,nom_joueur):
        return self.data_joueurs

    # Définition d'une méthode pour consulter les forces et faiblesses des types
    def get_types(self,type) :
        return self.data_type
        
    # Définition d'une méthode pour récupérer un pokémon de la BDD
    def get_pokemon(self,input_nom_joueur,input_nom_pokemon) :
        return self.data_joueurs[input_nom_joueur][input_nom_pokemon]

    # Définition d'une méthode pour ajouter les pokémons du joueur vaincu à la collection du joueur gagnant :
    def add_pokemon(self,input_nom_pokemon,input_nom_joueur):
        with open('joueurs.json','r+') as f :
            self.data_joueurs[input_nom_joueur]["pokemons"].append(input_nom_pokemon)

    # Définition de la méthode pour supprimer un joueur de la BDD, car n'a plus de pokémons actifs :
     def delete_joueur(self,input_nom_joueur):
         with open('joueurs.json','r+') as f :
            del self.data_joueurs[input_nom_joueur]["pokemons"]
            del self.data_joueurs[input_nom_joueur]


