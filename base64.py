import base64

# Message codé en Base64
message_base64 = "UkVTVEVSIENIQUNIySwgSUxTIE9OVCBEyUNPVVZFUlQgVk9UUkUgSVA="

# Décodage
message_clair = base64.b64decode(message_base64).decode("utf-8")

# Affichage du résultat
print("Message clair :", message_clair)
