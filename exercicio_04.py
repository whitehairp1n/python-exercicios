# Exercício 04

# fazer um programa que pede um número e imprime a tabuada dele, de 1 a 10


# numero = int(input("Digite um número: "))

# for i in range(1, 11):
# print(f"{numero} x {i} = {numero * i}")


numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



# - range(1, 11) vai de 1 até 10: o último número (11) nunca entra;
# - i é a variável do laço, ela muda a cada volta (1, 2, 3...);
# - tudo que está com recuo (Tab) dentro do for repete a cada volta;
# - o print com f"" mistura texto e variáveis: {numero} x {i} = {numero * i};
# - posso fazer a conta direto dentro das chaves do f-string.

