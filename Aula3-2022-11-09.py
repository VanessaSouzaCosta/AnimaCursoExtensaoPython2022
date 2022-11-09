print("Início da aula 3 (09/11/2022)")

contador = 1
#print(contador)
#contador += 1
#print(contador)

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1

# Laço For (Python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#lista
frutas = ["morango", "laranja", "pêra"]

# Mostra todas as frutas na lista
print(frutas)
# Quero exibir apenas a terceira fruta (pêra)
print(frutas[2])

# Exibir quantas frutas tem na lista
print(len(frutas)) # length = tamanho
# Incluir fruta nova
frutas.append("manga")

print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("Exemplo de frutas com While")
frutas.append("uva")

i=0
while(i<len(frutas)):
  print(frutas[i])
  i=i+1

