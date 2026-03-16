def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

print("Pozdrav! Mini kalkulator")
print("1 = seštevanje")
print("2 = odštevanje")

izbira = input("Kaj želiš narediti? (1 ali 2): ")

if izbira == "1":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {sestej(x, y)}")
elif izbira == "2":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {odstej(x, y)}")
else:
    print("Neveljavna izbira!")