from pathlib import Path



guia = Path("europa", "españa", "barcelona", "Sagrada Familia.txt")
en_europa = guia.relative_to(Path("europa"))
en_espana = guia.relative_to(Path("europa", "españa"))



print(en_espana)
print(en_europa)