#inserir 2 valores
a=int(input("Digite o primeiro número:"));
b=int(input("Digite o segundo número:"));

#ímpar ou par
print("O primeiro número digitado é:")
if a%2:
    print("ímpar")
else:
    print("Par")

#maior ou menor que 10
if a<10:
    print("Menor que 10")
elif a>10:
    print("Maior que 10")
elif a==10:
    print("Igual a 10")
#número ao quadrado
c = a*a
print(f'o quadrado deste número é: {c}')

#resto da divisão por 2
e = a%2
print(f'O resto da divisão deste número por 2 é: {e}')

print("*******************************************************")

#ímpar ou par
print("O segundo número é:")
if b%2:
    print("Ímpar")
else:
    print("Par")

#maior ou menor que 10
if b<10:
    print("Menor que 10")
elif b>10:
    print("Maior que 10")
elif b==10:
    print("Igual a 10")

#número ao quadrado
d = b*b
print(f'o quadrado deste número é: {d}')

#resto da divisão por 2
f = b%2
print(f'O resto da divisão deste número por 2 é: {f}')

print("*******************************************************")

#Soma dos dois números
g = a + b
print(f'A soma dos dois número é: {g}')
