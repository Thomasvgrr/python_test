def salaire_mensuel(salaire_annuel): 
    return salaire_mensuel / 12


 def salaire_hebdomadaire(salaire_mensuel):
     return salaire_mensuel / 4


def salaire_horaire(salaire_hebdomadaire,heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees


def main(): 
    
    salaire_annuel = float(input ("Saisissez votre saluaire annuel"))

    heures_travaillees = float(input ("Saisissez vos heures travaillés par semaine"))

    mensuel = salaire_mensuel(salaire_annuel)
    hebdomadaire = salaire_hebdomadaire(salaire_mensuel)
    horaire : salaire_horaire(salaire_hebdomadaire,heures_travaillees)

    print ("Votre salaire horaire est de ", horaire, "euros")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()