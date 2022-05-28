
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

joueur_1=['gertrude', 'Reptincel']
joueur_2=['albert', 'Noeunoeuf']

print(dic_joueur[0]["joueur"], dic_joueur[0]["ls_poke"])
print(dic_joueur[1]["joueur"], dic_joueur[1]["ls_poke"])
print("")

for i in range(len(dic_joueur)):
    ls_poke=dic_joueur[i]["ls_poke"]
    for p in range(len(ls_poke)):
        if joueur_2[0] == dic_joueur[i]["joueur"]:
            if joueur_2[1] == dic_joueur[i]["ls_poke"][p]["name"]["french"]:
                copie = dic_joueur[i]["ls_poke"][p]
                num_poke=p
                num_joueur=i
                supp=dic_joueur[num_joueur]["ls_poke"][num_poke]
            print(num_poke)
        
del dic_joueur[num_joueur]["ls_poke"][num_poke]
    #print(copie)
                        
for i in range(len(dic_joueur)):
    ls_poke=dic_joueur[i]["ls_poke"]
    if dic_joueur[i]["joueur"] == joueur_1[0] :
        dic_joueur[i]["ls_poke"][-1]=copie

print("")
print(dic_joueur[0]["joueur"], dic_joueur[0]["ls_poke"])
print(dic_joueur[1]["joueur"], dic_joueur[1]["ls_poke"])