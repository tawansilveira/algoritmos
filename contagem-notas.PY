valor = int(input("informe o valor do saque: "))

notas100 = int(valor/100)
resto = valor%100
print(f"{notas100} notas de 100")

notas50 = int((resto/50))
resto = resto%50
print(f"{notas50} notas de 50")

notas20 = int((resto/20))
resto = resto%20
print(f"{notas20} notas de 20")

notas10 = int((resto/10))
resto = resto%10
print(f"{notas10} notas de 10")

notas5 = int((resto/5))
resto = resto%5
print(f"{notas5} notas de 5")

notas2 = int((resto/2))
resto = resto%2
print(f"{notas2} notas de 2")

notas1 = int((resto/1))
resto = resto%1
print(f"{notas1} notas de 1")