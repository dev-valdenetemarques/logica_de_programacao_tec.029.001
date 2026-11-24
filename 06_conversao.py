# entrada de dados
nome = input("Informe o nome:")
idade = input("Informe sua idade:")
altura =input("Informe sua altura:").replace(',','.')

# conversao de tipo
idade = int(idade)
autura =float(altura)

# saida de dados
print(f"nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo {type(idade)}")
print(f"altura: {altura} metros. Tipo:{type(altura)}")