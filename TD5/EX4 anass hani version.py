#Question A:

"""
Chaque client peut être représenté par un dictionnaire ou un objet contenant :

numero : le numéro du client

date_arrivee : date d’arrivée en secondes depuis 8h

duree_traitement : durée du traitement en secondes

date_fin : date de fin de traitement (sera calculée lors de la simulation)

La file d’attente peut être une simple liste de clients, traitée dans l’ordre d’arrivée (FIFO).
"""

#Question B:

import random

INTERVALLE_MAX = 300         
DUREE_TRAITEMENT_MAX = 600   

def CreerListeClients():
    n = int(input("Nombre de clients : "))
    clients = []

    temps_courant = 0  
    for i in range(1, n+1):
        intervalle = random.randint(0, INTERVALLE_MAX)
        temps_courant += intervalle
        duree = random.randint(0, DUREE_TRAITEMENT_MAX)
        client = {
            "numero": i,
            "date_arrivee": temps_courant,
            "duree_traitement": duree,
            "date_fin": 0  
        }
        clients.append(client)
    
    return clients

#Question C:

def afficher_clients(clients):
    for client in clients:
        if client["numero"] == 1:
            debut = client["date_arrivee"]
        else:
            debut = max(clients[client["numero"]-2]["date_fin"], client["date_arrivee"])
        
        client["date_fin"] = debut + client["duree_traitement"]

        heures = 8 + client["date_fin"] // 3600
        minutes = (client["date_fin"] % 3600) // 60
        secondes = client["date_fin"] % 60

        print(f"Client {client['numero']} : Fin de traitement à {heures}h {minutes}min {secondes}sec")

