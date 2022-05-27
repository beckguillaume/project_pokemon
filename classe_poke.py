class pokemon():
    def __init__(self,nom):
        self.nom=nom
        #self.status="ok"
    def presentation_pokemon(self):
        print("nom",self.nom)
    def pokedex(self, nom):
        data_pokemon= open("pokedex.json","r")
        pokemonContent = data_pokemon.read()
        obj_pokemon = json.loads(pokemonContent)
        for i in range(0,800):
            if obj_pokemon[i]['name']['french'] == nom:
                type=obj_pokemon[i]['type']
                hp=obj_pokemon[i]['base']['HP']
                attaque=obj_pokemon[i]['base']['Attack']
                defense=obj_pokemon[i]['base']['Defense']
                sp_attaque=obj_pokemon[i]['base']['Sp. Attack']
                sp_def=obj_pokemon[i]['base']['Sp. Defense']
                vitesse=obj_pokemon[i]['base']['Speed']
        self.type=type
        self.hp=hp
        self.attaque=attaque
        self.defense=defense
        self.sp_attaque=sp_attaque
        self.sp_defense=sp_def
        self.vitesse=vitesse
        print(self.type)



poke_1=pokemon("Pikachu")
poke_1.pokedex("Pikachu")