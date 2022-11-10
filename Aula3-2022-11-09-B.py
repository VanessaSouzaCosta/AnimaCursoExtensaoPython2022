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
  imposto = preco_produto * 0.05
  return imposto

# Uso da função, imposto a calcular
preco = 299
imposto = calcular_imposto(preco)
print(imposto)
  



