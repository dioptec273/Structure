def somme_elements_distincts(tab1, tab2):
    somme = 0

    # Parcours du premier tableau
    for i in range(len(tab1)):
        trouve = False
        for j in range(len(tab2)):
            if tab1[i] == tab2[j]:
                trouve = True
                break
        if not trouve:
            somme += tab1[i]

    # Parcours du deuxième tableau
    for i in range(len(tab2)):
        trouve = False
        for j in range(len(tab1)):
            if tab2[i] == tab1[j]:
                trouve = True
                break
        if not trouve:
            somme += tab2[i]

    return somme


# Test avec les tableaux de l'exemple
tab1 = [3, 1, 7, 9]
tab2 = [2, 4, 1, 9, 3]

# Appel de la fonction avec passage par valeur
resultat = somme_elements_distincts(tab1[:], tab2[:])  # [:] pour passer une copie
print("Somme des éléments distincts :", resultat)