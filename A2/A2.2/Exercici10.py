frase = input("Introdueix una frase: ")

paraules = frase.split()

freq_paraules = {}
for paraula in paraules:
    if paraula in freq_paraules:
        freq_paraules[paraula] += 1
    else:
        freq_paraules[paraula] = 1

print(freq_paraules)
