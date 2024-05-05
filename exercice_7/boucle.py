def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    liste = input ("Entrer une liste de nombres séparés par une virgule: ")
    liste = liste.split(",")

    print("liste des nombres :", liste)


    somme = 0 
    for nombre in liste:
        somme += int(nombre)
        print("somme des nombre :", somme)

    moyenne = somme / len(liste)
    print("somme des nombres :", moyenne)

    nombre_sup_moyenne = 0
    for nombre in liste:
        if int(nombre) > moyenne:
            nombre_sup_moyenne += 1
    print("Nombre de nombres supérieurs à la moyenne :", nombre_sup_moyenne)

    nombre_pairs = 0
    i = 0
    while i < len(liste):
        if int(liste[i]) % 2 == 0:
            nombre_pairs += 1
        i += 1
    print("Nombre de nombres pairs :", nombre_pairs)







# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
