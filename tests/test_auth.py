from src.auth import connecter

def test_connexion_valide():
    res = connecter("alice@mail.com", "votre_password_test")
    assert res["statut"] == "connecte"
    assert res["email"] == "alice@mail.com"

def test_email_vide():
    try:
        connecter("", "secret")
        assert False, "Doit lever une exception"
    except ValueError:
        pass
