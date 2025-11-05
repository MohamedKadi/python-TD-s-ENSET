import numpy as np

# etape1

vehicules = [
    {"id": 1, "position": np.array([0, 0]), "disponible": True},
    {"id": 2, "position": np.array([5, 1]), "disponible": True},
    {"id": 3, "position": np.array([2, 3]), "disponible": True},
    {"id": 4, "position": np.array([8, 8]), "disponible": True},
]


clients_en_attente = [
    {"id_client": 101, "position": np.array([1, 0])},
    {"id_client": 102, "position": np.array([6, 2])},
    {"id_client": 103, "position": np.array([3, 4])},
    {"id_client": 104, "position": np.array([9, 9])},
]

# etape2
def calculer_distance(pos1, pos2):
    diff = pos1 - pos2
    return float(np.sqrt((diff ** 2).sum()))

# etape3
assignations = [] 

for client in clients_en_attente:
    vehicules_dispos = list(filter(lambda v: v["disponible"], vehicules))

    if not vehicules_dispos:
        print("aucune vehicule disponible")
        break

    distances = list(map(
        lambda v: calculer_distance(client["position"], v["position"]),
        vehicules_dispos
    ))

    couples = list(zip(distances, vehicules_dispos))

    distance_min, vehicule_elu = min(couples, key=lambda x: x[0])

    print(f"Client {client['id_client']} -> Véhicule {vehicule_elu['id']} (distance {distance_min:.2f})")
    assignations.append((client["id_client"], vehicule_elu["id"]))

    vehicule_elu["disponible"] = False

# etape4
print("\nAssignations finales :")
print(assignations)

print("\nÉtat final des véhicules :")
for v in vehicules:
    print(f"Véhicule {v['id']} | Position={v['position']} | Disponible={v['disponible']}")
