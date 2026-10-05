import bcrypt

pw = b" incontrastablemente " # Define la contraseña. La b antes de las comillas indica que es un objeto de tipo bytes, que es el formato que 
                              # requiere bcrypt.

hashed = bcrypt.hashpw(pw, bcrypt.gensalt()) # hashpw toma la contraseña en bytes y le aplica un s

print(hashed)

print(bcrypt.checkpw(pw, hashed)) # compara la contraseña en texto con el hash. Automáticamente extrae el salt del string del hash, vuelve a 
                                  # calcular todo y verifica si coincide, devolviendo True o False


# Con la salida del código anterior, repita lo realizado en 3)
# Para intentar un ataque de diccionario aquí, tendrías que leer el archivo de texto, convertir cada palabra a bytes (.encode()) y usar la función 
# bcrypt.checkpw(palabra_diccionario, hashed) en un bucle for para ver si alguna arroja True.
# 
# b) ¿Es capaz de obtener la contraseña? Justifique su respuesta
# No (o sería extremadamente ineficiente). Hay dos razones. A nivel criptográfico, bcrypt es intencionalmente lento; verificar miles de palabras del 
# diccionario tomará una cantidad de tiempo y procesamiento brutal comparado con SHA-256, deteniendo el ataque de fuerza bruta. Además, a nivel de 
# código, la variable original incluye espacios (b" incontrastablemente "), por lo que las palabras exactas de tu archivo diccionario.txt nunca 
# coincidirán.   
# 
# c) ¿Cómo podría obtener el mismo código (a nivel de seguridad) pero con la librería cryptography?
# Se lograría utilizando una función de derivación de claves basada en contraseñas (PBKDF) que incluya un salt aleatorio y un alto número de 
# iteraciones. En la librería cryptography, esto se hace usando el módulo PBKDF2HMAC. El proceso requiere usar os.urandom(16) para generar el salt, 
# definir un número de iteraciones (por ejemplo, 390000), usar un algoritmo base como SHA-256 internamente, y finalmente usar la función derive() 
# para obtener la clave segura.