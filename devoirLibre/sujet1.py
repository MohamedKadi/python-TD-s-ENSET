
#etape 1

entrepots = {
    "entrepot1":{
        "stock":{"produit1":1,"produit2":2},
        "cout":55,
    },
    "entrepot2":{
        "stock":{"product1":1,"produit2":2},
        "cout":25,
    } #etc
}

client_cmd = {"produit1":2,"peoduit2":3} #etc
#etape 2
from sympy import *
cout_exp = input("entrer le cout comme cette form (ex: 2 * quantite + 5).")

quantite = symbols('quantite')

exp_symbolique = sympify(cout_exp)
print(exp_symbolique)

fonc_exp = lambdify((quantite),exp_symbolique,'numpy')
#result = fonc_exp(10)
#print(result)


#etape 3
def trouver_solution(commande, entrepots):
    plan_approvisionnement = {}
    cout_total = 0
    sorted_entrepots = sorted(entrepots.items(),key=lambda item: item[1]['cout'])
    for nom_entrepot , infos in sorted_entrepots:
        #print(nom_entrepot + " info "+ str(infos))
        for produit, qte in list(commande.items()):
            if qte <= 0:
                continue

            dispo = infos['stock'].get(produit, 0) # si le produit n'est exist pas

            if dispo <= 0:
                continue

            pris = min(qte, dispo)

            infos['stock'][produit] = dispo - pris

            commande[produit] = qte - pris
            plan_approvisionnement.setdefault(nom_entrepot, {})
            plan_approvisionnement[nom_entrepot][produit] = (
                plan_approvisionnement[nom_entrepot].get(produit, 0) + pris
            )

            cout_total += fonc_exp(pris) * infos['cout']

    return plan_approvisionnement, cout_total

entrepots = {
    "Entrepot_A": {
        "stock": {"ProduitX": 5, "ProduitY": 8, "ProduitZ": 0},
        "cout": 50
    },
    "Entrepot_B": {
        "stock": {"ProduitX": 3, "ProduitY": 2, "ProduitZ": 4},
        "cout": 30
    },
    "Entrepot_C": {
        "stock": {"ProduitX": 6, "ProduitY": 5, "ProduitZ": 10},
        "cout": 70
    }
}

commande = {
    "ProduitX": 8,
    "ProduitY": 10,
    "ProduitZ": 5
}

#etape4
plan_app, cout_total = trouver_solution(commande, entrepots)
print(plan_app)
print("\n=== PLAN D'APPROVISIONNEMENT ===")
for entrepot, produits in plan_app.items():
    for produit, quantite in produits.items():
        print(f"Prendre {quantite} de {produit} chez {entrepot}")

print(f"\nCoût total: {cout_total}")
