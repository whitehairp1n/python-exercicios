# Exercício 03

# fazer um programa que pede duas notas e imprime a média

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota1 + nota2) / 2
# print(f"Média: {media}")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2

print(f"Média: {media}")


# - float() converte o texto digitado em número com casas decimais (3.5, 7.25)
# - se eu usasse int(), uma nota como 7.5 daria erro
# - os parênteses em (nota1 + nota2) / 2 são importantes: sem eles, só a nota2 seria dividida por 2
# - a divisão com / sempre devolve float, por isso 8 e 6 dão 7.0 e não 7
# - o nome da variável precisa ser igual onde eu uso: nota1 e nota2 são variáveis diferentes
