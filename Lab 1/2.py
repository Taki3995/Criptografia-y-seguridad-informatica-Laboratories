from cryptography.hazmat.primitives import hashes

def hash_password(pw): # define la función para hashear la contraseña
 digest = hashes.Hash(hashes.SHA256()) #! Error, no incorpora el salt aleatorio, lo que hace que el hash sea vulnerable a ataques de diccionario y rainbow tables
 digest.update(pw.encode()) # Actualiza el objeto de hash con la contraseña codificada en bytes
 return digest.finalize().hex()

pw1 = "password123"

pw2 = "password123"

print(hash_password(pw1)) # Imprime el hash de la primera contraseña

print(hash_password(pw2)) # Imprime el hash de la segunda contraseña, que es la misma que la primera, por lo que el hash será igual

# 3
common = diccionario

target = hash_password("incontrastablemente")

for pw in common:
 if hash_password(pw) == target:
 print("Found:", pw)