# Criação de Funções

preco = 1999.90

# Calcular apenas 5% de imposto, guardar na variável imposto e exibir na tela
imposto = preco*0.05
print(imposto)

preco2 = 100
imposto2 = preco2*0.05
print(imposto2)

# Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna
# Declaração de função (como funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

# Uso da função, imposto a calcular e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%): {imposto}")

#Explicação de variável local x global
print(preco) #????
preco_produto = 100
print(preco_produto) #????


#Calcular imposto com aliquota a 7%

valores = [1.99, 24.50, 78.27, 1515.5]
# Calcular imposto dos 4 valores e exibir na tela "O imposto de x é (preco1, preco2)"
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")



