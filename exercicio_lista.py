#1)Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros = list(range(1,11))
# for x in numeros:
#     print(x**2)

#2)Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# lista = ["Python", "Java", "C++", "JavaScript"]
# lista.remove("C++")
# lista.insert(2,"Ruby")
# print(lista)

#3)Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# livro01: dict = {
#    "título":"Principe Engenheria",
#    "Autor":"Arthurito",
#    "Ano": 1994,
# }
# livros2: dict = {
#    "título":"Rei eng",
#    "Autor":"wagnito",
#    "Ano": 1989,
# }
# livros: list =[]
# livros.extend([livro01,livros2])
# for livro in livros:
#     print("{")
#     for chave, valor in livro.items():
#         print(f'   "{chave}": "{valor}",')
#     print("}")

#4)Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))   

#5)Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
#Calcule o preço total da lista de compras.

#  lista=["maçã", "banana", "cereja"]
#  dictt={"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#  total = sum(dictt[item] for item in lista)
#  print(f"Preço total: {total}")

#6)Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))
# print(emails_unicos)

#7)Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [22, 15, 30, 17, 18]
# for idade in idades:
#     if idade >= 18:
#         print(idade)

##idades_validas = [idade for idade in idades if idade >= 18]  #utlizando "Comprehension"
##print(idades_validas)

#8)Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# pessoas_ordenadas = sorted(pessoas, key=lambda x: x["nome"])
# # Exibe a lista de pessoas ordenadas
# for pessoa in pessoas_ordenadas:
#     print(pessoa)

#9)Dado um conjunto de números, calcular a média.
# numeros = [10, 20, 30, 40, 50]

# media = sum(numeros)/ len(numeros)
# print(media)

#10)Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = [par for par in valores if par % 2==0]
# impares = [impar for impar in valores if impar % 2!=0]
# print(pares)
# print(impares)

#11)Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# for produto in produtos:
#     if produto["id"] == 3:
#         produto["preço"] = 250

# print(produtos)

#12)Dados dois dicionários, fundi-los em um único dicionário.
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dic_total = dicionario1 | dicionario2
# print(dic_total)

#13)Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}
# print(estoque_positivo)

#14) Dado um dicionário, criar listas separadas para suas chaves e valores.

# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

# print("Chaves:", chaves)
# print("Valores:", valores)

#15)Dada uma string, contar a frequência de cada caractere usando um dicionário.

# texto = "engenharia de dados"
# frequencia = {}

# for caractere in texto:
#     if caractere in frequencia:
#         frequencia[caractere] += 1
#     else:
#         frequencia[caractere] = 1

# print(frequencia)

