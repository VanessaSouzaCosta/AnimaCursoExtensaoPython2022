# Pede nome do aluno e sua nota de 0 a 10, se 10 mostra "você é bichão mermo..."
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota de 0 a 10: "))
if nota == 10:
  print (f"{nome}, você é o bichão mermo...")
elif (nota >= 6 and nota <10):
  print (f"{nome}, bom trabalho")
elif (nota < 0 or nota > 10):
  print (f"{nome}, digitou uma nota invalida")
else:
  print(f"Burro, dá {nota} pra ele!")
