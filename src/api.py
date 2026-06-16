utilisateurs = []

def ajouter_utilisateur(nom, email):
    utilisateurs.append({"nom": nom, "email": email})
    return utilisateurs
# Mise a jour API
def lister_utilisateurs(): return utilisateurs
def supprimer_utilisateur(email): pass
# TODO: add pagination
