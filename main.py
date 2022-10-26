# Comando input(): permite o usuario digitar algo
nome = input("Digite seu nome: ")

#pede idade - forçando numero int
idade = int(input("Qual é a sua idade: "))

# Comando de saída, exibir na tela
print(nome)
print(f"Boa noite, seu nome é {nome}")

# Exibir idade
print(f"{nome}, sua idade é {idade} anos")

# Mostrar dobro da idade informada
dobro = idade*2
print("o dobro da idade informada é {}".format(dobro))
