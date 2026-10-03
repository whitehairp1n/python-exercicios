# Exercício 05

# fazer um programa que pede números até digitar 0 imprime a soma.


# soma = 0

# while True:
# pedir o número com int(input(...))
# se o número for 0, parar com break
# somar o número na variável soma

# print(f"Soma: {soma}")


soma = 0

while True:
    numero = int(input("Digite um número (0 para imprimir a soma): "))

    if numero == 0:
        break

    soma += numero

print(f"Soma: {soma}")
