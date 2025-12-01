preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25}

preus_alts = {producte: preu for producte, preu in preus.items() if preu > 20}

print(preus_alts)
