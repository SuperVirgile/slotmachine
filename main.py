import random

MAX_LIGNES = 3
MAX_PARI = 100
MIN_PARI = 1

LIGNES = 3
COLONNES = 3

compte_symbole = {
	"A" : 2,
	"B" : 4,
	"C" : 6,
	"D" : 8
}

valeur_symbole = {
	"A" : 5,
	"B" : 4,
	"C" : 3,
	"D" : 2
}

def verification_gains(colonnes, lignes, pari, valeurs):
	gains = 0
	lignes_gagnees = []
	for ligne in range(lignes):
		symbole = colonnes[0][ligne]
		for colonne in colonnes:
			symbole_a_verifier = colonne[ligne]
			if symbole != symbole_a_verifier:
				break
		else :
			gains += valeurs[symbole] * pari
			lignes_gagnees.append(ligne + 1)

	return gains, lignes_gagnees


def obtenir_resultat_slotmachine(lignes, colonnes, symboles):
	tout_les_symboles = []
	for symboles, compte_symboles in symboles.items():
		for _ in range(compte_symboles):
			tout_les_symboles.append(symboles)

	cols = []
	for _ in range(colonnes):
		colonne = []
		symboles_courant = tout_les_symboles[:]
		for _ in range(lignes):
			valeur = random.choice(symboles_courant)
			symboles_courant.remove(valeur)
			colonne.append(valeur)

		cols.append(colonne)

	return cols

def print_slotmachine(colonnes):
	for ligne in range(len(colonnes[0])):
		for i, colonne in enumerate(colonnes):
			if i != len(colonnes) - 1:
				print(colonne[ligne], end = " | ")
			else :
				print(colonne[ligne], end = "")
		print()


def depot():
	while True:
		montant = input("Combien voudriez vous déposer ? € ")
		if montant.isdigit():
			montant = int(montant)
			if montant > 0:
				break
			else :
				print("Le montant doit être supérieur à 0.")

		else :
			print("Entrez un nombre svp.")

	return montant


def obtenir_montant_lignes():
	while True:
		lignes = input("Entrez le nombre de lignes sur lequel parier (1-" + str(MAX_LIGNES) + ") ? ")
		if lignes.isdigit():
			lignes = int(lignes)
			if 1 <= lignes <= MAX_LIGNES:
				break
			else :
				print("Entrez un nombre valide de lignes.")

		else :
			print("Entrez un nombre svp.")

	return lignes

def obtenir_pari():
	while True:
		montant = input("Combien voudriez vous parier sur chaque ligne ? € ")
		if montant.isdigit():
			montant = int(montant)
			if MIN_PARI <= montant <= MAX_PARI:
				break
			else :
				print(f"Le montant doit être entre {MIN_PARI}€ - {MAX_PARI}€.")

		else :
			print("Entrez un nombre svp.")

	return montant


def jeu(balance):
	lignes = obtenir_montant_lignes()
	while True:
		pari = obtenir_pari()
		pari_total = pari * lignes

		if pari_total > balance:
			print(f"Vous n'avez pas assez pour parier ce montant, vous avez actuellement {balance}€ disponible.")
		else :
			break

	print(f"Vous parier {pari}€ sur {lignes} lignes. Le pari total est d'un montant de : {pari_total}€.")

	slots = obtenir_resultat_slotmachine(LIGNES, COLONNES, compte_symbole)
	print_slotmachine(slots)
	gains, lignes_gagnees = verification_gains(slots, lignes, pari, valeur_symbole)
	print(f"Vous avez gagné {gains}€.")
	print(f"Vous avez gagné sur les lignes :", *lignes_gagnees)
	return gains - pari_total

def main():
	balance = depot()
	while True:
		print(f"Le dépot est de : {balance}€")
		roulement = input("Appuyer sur 'entrer' pour jouer (q pour quitter).")
		if roulement == 'q':
			break
		balance += jeu(balance)

	print(f"Vous avez quitté avec {balance}€")

main()