# Fonction qui calcule le produit scalaire de deux vecteurs
def dot_product(v1, v2):
    ps = 0  # Initialiser la variable du produit scalaire

    # Parcourir chaque composante des vecteurs
    for i in range(len(v1)):
        ps += v1[i] * v2[i]  # Ajouter le produit des composantes à ps

    return ps  # Retourner le produit scalaire

# Fonction pour tester si des paires de vecteurs sont orthogonaux
def tester_orthogonalite(paires_vecteurs):
    for v1, v2 in paires_vecteurs:
        ps = dot_product(v1, v2)  # Calculer le produit scalaire

        # Si le produit scalaire est nul, les vecteurs sont orthogonaux
        if ps == 0:
            print(f"{v1} et {v2} sont orthogonaux.")
        else:
            print(f"{v1} et {v2} ne sont pas orthogonaux.")

# Exemple de test avec plusieurs paires de vecteurs
vecteurs = [
    ([1, 2], [2, -1]),         # Non orthogonaux : produit scalaire = 0 ?
    ([1, 0], [0, 1]),          # Orthogonaux : produit scalaire = 0
    ([1, 2, 3], [4, 5, 6])     # Non orthogonaux
]

# Lancer le test
tester_orthogonalite(vecteurs)