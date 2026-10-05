from cryptography.hazmat.primitives import hashes

def hash_password(pw): # define la función para hashear la contraseña
 digest = hashes.Hash(hashes.SHA256()) #! Error, no incorpora el salt aleatorio, lo que hace que el hash sea vulnerable a ataques de diccionario y rainbow tables
 digest.update(pw.encode()) # Actualiza el objeto de hash con la contraseña codificada en bytes
 return digest.finalize().hex()

pw1 = "password123"

pw2 = "password123"

print(hash_password(pw1)) # Imprime el hash de la primera contraseña

print(hash_password(pw2)) # Imprime el hash de la segunda contraseña, que es la misma que la primera, por lo que el hash será igual

# ¿Qué observa? ¿Hay algún problema de seguridad?
# La consola imprime dos veces el mismo valor hexadecimal porque la contraseña es identica. por lo que si un atacante roba la base de datos de de hashes, 
# podrá agrupar a los usuarios que tengan el mismo hash y deducir que comparten la misma contraseña. Peor aún, permite el uso de "Rainbow Tables" 
# (tablas gigantes precomputadas de hashes de contraseñas comunes). Si el atacante busca ese hash en su tabla y encuentra que corresponde a 
# "password123", habrá comprometido a todos los usuarios que usen esa clave en un solo paso.

# ¿Qué problema hay aquí con SHA256?
# Su extremada eficiencia y velocidad computacional. Fue diseñado para procesar grandes volúmenes de datos muy rápido (por ejemplo, para verificar 
# que un archivo descargado de internet no esté corrupto). En seguridad de contraseñas, la velocidad beneficia al atacante: usando hardware moderno,
# especialmente tarjetas gráficas (GPUs), un atacante puede generar miles de millones de hashes SHA-256 por segundo para probar combinaciones 
# rápidamente. Un buen algoritmo para contraseñas debe ser intencionalmente lento y costoso para la CPU/memoria.

# 3
common = diccionario

target = hash_password("incontrastablemente")

for pw in common:
 if hash_password(pw) == target:
 print("Found:", pw)