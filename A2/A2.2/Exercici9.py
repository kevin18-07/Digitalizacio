alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7}
}

millor_alumne = max(alumnes, key=lambda alumne: alumnes[alumne]['nota_final'])

print(millor_alumne)
