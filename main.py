import random

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("Dime la longitud de la contraseña: "))
password = ""
while True:
    for i in range(long):
        element = random.choice(char)
        password += element
    print("Tu contraseña generada es: ", password)
    conf = input("Quieres generar otra contraseña y o n")
    if conf == "n":
        break
    if conf == "y":
        password = ""
