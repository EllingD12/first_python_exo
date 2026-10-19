name = input("Quel est votre prénom ? ")

annee_texte = input("Quelle est votre année de naissance ? ")
annee_naissance = int(annee_texte)

age = 2026 - annee_naissance

print(f"Bonjour {name}, vous avez aujourd'hui {age} ans")