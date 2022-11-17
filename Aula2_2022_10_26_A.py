# Comando input(): permite o usuario digitar algo
nome = input("Digite seu nome: ")

# Pede idade - forçando numero int
idade = int(input("Qual é a sua idade: "))

# Comando de saída, exibir na tela
print(f"Boa noite, seu nome é {nome}")
# Exibir idade
print(f"{nome}, sua idade é {idade} anos")

# Mostrar dobro da idade informada
dobro = idade*2
print("o dobro da idade informada é {}".format(dobro))

# Estrutura condicional - Famoso "se" (if)
# Se a pessoa for maior de idade, mostre "você é maior de idade, já pode beber ou dirigir"
if idade >= 18:
  print("você é maior de idade, já pode beber ou dirigir")
else:
  print("você é jovem ainda, jovem ainda...")

# E se quiser perguntar o gênero (M = Masculino e F = Feminino) mostre "... precisa/precisou prestar serviço militar obrigatório"
genero = input("Qual gênero você se identifica mais? Coloque M para masculino ou F para feminino: ")
if idade >= 18 and genero == "M":
  print("você é maior de idade, já pode beber ou dirigir ... e precisa/precisou prestar serviço militar obrigatório")