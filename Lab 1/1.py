from cryptography.hazmat.primitives import hashes # Importa libreria necesaria para trabajar con hashess

def sha256_hash(password): # Funcion que transforma la contraseña
 digest = hashes.Hash(hashes.SHA256()) # Crea un objeto de hash SHA256
 digest.update(password.encode()) # Actualiza el objeto de hash con la contraseña codificada en bytes
 return digest.finalize().hex() # Devuelve el hash final en formato hexadecimal

def almacenar_password(password): # Simula el almacenamiento de la contraseña en la base de datos
 return sha256_hash(password)

def verificar_password(password, hash_almacenado): # Compara la contraseña ingresada con el hash almacenado
 return sha256_hash(password) == hash_almacenado

# Registro
hash_usuario = almacenar_password("123456")

# Login
if verificar_password("123456", hash_usuario):
 print("Acceso concedido")


else:
 print("Acceso denegado")


# Qué algoritmo hash se está utilizando?
# SHA-256 (Secure Hash Algorithm de 256 bits).

# Las contraseñas se están almacenando en texto plano?
# No. Cuando se llama a almacenar_password("123456"), la contraseña original es procesada y lo que realmente se almacena 
# en la variable hash_usuario es la representación en hexadecimal de su hash.

# Aunque no estén en texto plano, ¿ves algún problema de seguridad importante?
# Sí, la implementación es vulnerable. Al no incluir un salt aleatorio, el sistema es susceptible a ataques mediante 
# "Rainbow Tables" (tablas precomputadas de hashes) o ataques de diccionario. Además, al usar un algoritmo rápido como 
# SHA-256 en lugar de una función derivadora de claves diseñada específicamente para ser costosa computacionalmente 
# (como bcrypt, Argon2 o PBKDF2), se facilita enormemente la rotura del hash por fuerza bruta.