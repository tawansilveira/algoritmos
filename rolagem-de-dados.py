# simulação de rolagem de dados

import random
def rolar_Dados(tamanho):
    return random.randint(1, tamanho)

jogar_denovo = True
while jogar_denovo:
    a = input(" ")
    b = a.split("d" or "D")
    res = 0
    for i in range(int(b[0])):
        valor = rolar_Dados(int(b[1]))
        res += valor
        print(f'Dado {i+1}: {valor}')
    print(f'Resultado final: {res}')

    print("Jogar novamente?")
    jogar_denovo = ("s") in input().lower()
else:
    jogar_denovo = ("n")
    print("Fim de jogo!")
