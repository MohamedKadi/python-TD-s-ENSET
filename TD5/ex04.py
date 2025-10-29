

#client{num,date_arrive, date_debut_traitement, date_fin_traitement}
# file d'attend
# between 2 clients random num from 0 to INTERVALLE_MAX
# time during the traitement from 0 to DUREE_TRAITEMENT_MAX

import random

INTERVALLE_MAX = 300         
DUREE_TRAITEMENT_MAX = 600

def CreerListeClients(n):
    queue = []
    random_intervalle = random.randint(0,INTERVALLE_MAX)
    random_traitement_time = random.randint(0, DUREE_TRAITEMENT_MAX)
    courant_temp = 28800
    for i in range(1,n+1):
        courant_temp += random_intervalle
        client = {
            "num": i,
            "date_arrive": courant_temp,
            "date_debut_traitement" : random_traitement_time,
            "date_fin_traitement":0
        }
        queue.append(client)
    return queue
"""
date_arr                    d_debut traitement        d_fin(d_debut traitement + random)
8:00        client 1        8:00                    -> 8:05
8:02        client 2        8:05                    -> 8:15
8:05        client 3        8:15                    -> 8:16
"""

def affiche_Clients(clients):
    index = 1
    for client in clients:
        if(client["num"] == 1):
            debut = 28800 + client["date_debut_traitement"]

        client["date_fin_traitement"] = debut + client["date_debut_traitement"]

        h_date_arrive = client["date_arrive"] // 3600
        min_date_arrive = (client["date_arrive"] % 3600) // 60
        sec_date_arrive = (client["date_arrive"] % 60) // 60

        h_date_fin_traitement = client["date_fin_traitement"] // 3600
        min_date_fin_traitement = (client["date_fin_traitement"] % 3600) // 60
        sec_date_fin_traitement = (client["date_fin_traitement"] % 60) // 60
        print(f"client num : {index} ==============================================================")
        print(f"date Arrivé: {h_date_arrive}:{min_date_arrive}:{sec_date_arrive}")
        print(f"date debut traitement: {(debut//3600)}:{((debut%3600)//60)}:{((debut%60)//60)}")
        print(f"date Fin: {h_date_fin_traitement}:{min_date_fin_traitement}:{sec_date_fin_traitement}")
        index += 1
        debut = client["date_fin_traitement"]

        
file = CreerListeClients(3)
affiche_Clients(file)