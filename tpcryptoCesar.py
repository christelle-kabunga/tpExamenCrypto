from collections import Counter

def cesar_dechiffrement_analyse_freq(texte_chiffre):
    frequences_anglais = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'.lower()
    compteur = Counter(texte_chiffre.lower())
    lettres_ordonnees = [x[0] for x in compteur.most_common() if x[0].isalpha()]
    
    solutions = []
    for i in range(min(5, len(lettres_ordonnees))):
        decalage = (ord(lettres_ordonnees[i]) - ord('e')) % 26
        texte_dechiffre = ''.join(
            chr(((ord(c) - ord('a') - decalage) % 26) + ord('a')) if c.isalpha() else c for c in texte_chiffre.lower()
        )
        solutions.append((decalage, texte_dechiffre))
    
    return solutions

# Demander à l'utilisateur d'entrer le message chiffré
if __name__ == "__main__":
    texte_chiffre = input("Entrez le message chiffré à déchiffrer : ")
    resultats = cesar_dechiffrement_analyse_freq(texte_chiffre)
    for i, (decalage, texte) in enumerate(resultats):
        print(f"Essai {i+1} (Décalage {decalage}): {texte}")
