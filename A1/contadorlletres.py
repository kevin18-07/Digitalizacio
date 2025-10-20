paraula = input("Introdueix una paraula: ")
lletra = input("Introdueix la lletra que vols buscar: ")

comptador = 0

for i in range(len(paraula)):
    if paraula[i] == lletra:
        comptador += 1
        print(f"Lletra '{lletra}' trobada a la posició {i}")

print(f"\nTotal de '{lletra}' trobades: {comptador}")
