# Exercício 02

# fazer um programa que pede um número e imprime se ele é par ou ímpar


# numero = int(input("Digite um número: "))


# if numero % 2 == ___:
# print("par")
# else:
# print("ímpar")


numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("par")
else:
    print("ímpar")


# o input sempre devolve texto, então precisa do int() pra fazer a conta
# o % é o resto da divisão, 8 % 2 dá 0 e 7 % 2 dá 1
# número par tem resto 0 quando dividido por 2
# o == compara dois valores, já o = só guarda um valor na variável
# o if e o else terminam com dois pontos
# o que fica recuado embaixo do if/else é o que roda em cada caso
# se digitar uma letra em vez de número, o programa dá erro (o int() não consegue converter)
# o zero também é par, porque 0 % 2 dá 0


# erro que cometi: deixei um ? no lugar do número e deu SyntaxError
# NameError quer dizer que o Python não sabe o que é aquele nome


