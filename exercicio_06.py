# Exercício 06

# fazer um programa que pede 5 nomes, guarda numa lista e imprime os nomes em ordem alfabética.

# nomes = []

# for i in range(5):
# pedir o nome com input(...)
# guardar na lista com nomes.append(...)

# ordenar com sorted(nomes) e mostrar com print(...)


nomes = []

for i in range(5):
    nome = input(f"Nome {i + 1}: ")
    nomes.append(nome)

ordenados = sorted(nomes)
print(", ".join(ordenados))


# - nomes = [] cria uma lista vazia, que vai guardando os itens em ordem;
# - append() coloca um item no final da lista;
# - range(5) repete 5 vezes: 0, 1, 2, 3 e 4;
# - sorted() devolve uma lista nova em ordem alfabética, sem mudar a original;
# - input() sempre devolve texto, por isso não precisa de int() aqui.
