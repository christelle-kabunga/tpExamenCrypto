from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def generer_cle():
    return get_random_bytes(16)  # Clé AES 128 bits

def chiffrer_aes(texte, cle, mode):
    iv = get_random_bytes(16) if mode != AES.MODE_ECB else None
    cipher = AES.new(cle, mode, iv) if iv else AES.new(cle, mode)
    texte_chiffre = cipher.encrypt(pad(texte.encode(), AES.block_size))
    return base64.b64encode(iv + texte_chiffre).decode() if iv else base64.b64encode(texte_chiffre).decode()

def dechiffrer_aes(texte_chiffre, cle, mode):
    data = base64.b64decode(texte_chiffre)
    iv = data[:16] if mode != AES.MODE_ECB else None
    cipher = AES.new(cle, mode, iv) if iv else AES.new(cle, mode)
    texte_dechiffre = unpad(cipher.decrypt(data[16:]), AES.block_size) if iv else unpad(cipher.decrypt(data), AES.block_size)
    return texte_dechiffre.decode()

# Modes disponibles
modes = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CTR": AES.MODE_CTR,
    "OFB": AES.MODE_OFB,
    "CFB": AES.MODE_CFB,
}

# Interface utilisateur
if __name__ == "__main__":
    texte = input("Entrez le texte à chiffrer : ")
    mode_str = input("Choisissez le mode (ECB, CBC, CTR, OFB, CFB) : ").upper()
    if mode_str not in modes:
        print("Mode invalide !")
    else:
        cle = generer_cle()
        mode = modes[mode_str]
        texte_chiffre = chiffrer_aes(texte, cle, mode)
        texte_dechiffre = dechiffrer_aes(texte_chiffre, cle, mode)
        print(f"\nTexte chiffré : {texte_chiffre}")
        print(f"Texte déchiffré : {texte_dechiffre}")
