from ast import While

n1 = float(input("Qual a temperatura?"))

print("Escolha a escala de temperatura desejada:\n")
print("[F]   -   Farenheit")
print("[C]   -   Celsius")
print("[K]   -   Kelvin")

def F_to_C():
    f1 = (n1 - 32) * 5/9
    print(f"A temperatura é:{f1:.2f} Graus Celsius")

def F_to_K():
    f2 = (n1 - 32) * 5/9 + 273.15 
    print(f"A temperatura é:{f2:.2f} Graus Kelvin")

def C_to_F():
    c1 = (n1 * 9/5) + 32
    print(f"A temperatura é:{c1:.2f} Graus Farenheit")

def C_to_K():
    c2 = n1 + 273.15 
    print(f"A temperatura é:{c2:.2f} Graus Kelvin")

def K_to_F():
    k1 = n1 - 273.15
    k3 = k1 * 1.8 + 32
    print(f"A temperatura é:{k3:.2f} Graus Farenheit")

def K_to_C():
    k2 = n1 - 273.15 
    print(f"A temperatura é:{k2:.2f} Graus Celsius")

resposta = input("")
if resposta == "F":
    F_to_C()
    F_to_K()
elif resposta == "C":
    C_to_F()
    C_to_K()
elif resposta == "K":
    K_to_F()
    K_to_C()
else:
    print("Opção Inválida, tente novamente!")
    print("K para Kelvin, F para Farenheit & C para Celsius")
