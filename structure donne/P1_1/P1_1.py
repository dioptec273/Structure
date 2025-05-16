def somme_elements_distincts(tab1, tab2):
    # Fusionner les deux listes pour pouvoir parcourir tous les éléments
    union = tab1 + tab2
    somme = 0  # Initialiser la somme des éléments distincts à 0

    # Parcourir chaque élément de la liste fusionnée
    for elem in union:
        # Si l'élément est dans un seul des deux tableaux (donc distinct)
        if (elem in tab1 and elem not in tab2) or (elem in tab2 and elem not in tab1):
            somme += elem  # Ajouter cet élément à la somme

    return somme  # Retourner la somme totale des éléments distincts

# Exemple d’utilisation
serie1 = [3, 1, 7, 9]
serie2 = [2, 4, 1, 9, 3]
# Affiche le résultat : 13 (car les éléments distincts sont 7, 2, 4)
print("Sortie :", somme_elements_distincts(serie1, serie2))