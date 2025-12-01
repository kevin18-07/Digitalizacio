notes = {'Anna': [8, 9, 7], 'Pau': [5, 6, 6]}

for alumne, llistes_notes in notes.items():
    mitjana = sum(llistes_notes) / len(llistes_notes)
    print(f"{alumne} → {mitjana:.2f}")
