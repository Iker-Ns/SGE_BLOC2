from read_registre import read_reg

results = read_reg()

for result in results:
    print(f"Nom: {result[0]}, Adreça: {result[1]}, Telèfon: {result[2]}, Email: '{result[3]}', Neixament: {result[4]}")
    print("\n")