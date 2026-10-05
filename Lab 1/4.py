import bcrypt

pw = b" incontrastablemente "

hashed = bcrypt.hashpw(pw, bcrypt.gensalt())

print(hashed)

print(bcrypt.checkpw(pw, hashed))