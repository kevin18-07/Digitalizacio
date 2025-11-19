text = input("dime la palabra y caracteres")
text2 = input("dime la palabra y caracteres")

coincidencies = 0

longitud = min(len(text), len(text2))

for i in range(longitud):
    if text[i] == text2[i]:
        coincidencies += 1

print(f"Nombre de caràcters que coincideixen en la mateixa posició: {coincidencies}")
