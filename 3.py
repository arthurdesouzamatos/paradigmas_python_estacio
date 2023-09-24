#Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.
lista = []
pares = []
impares = []

for x in range (20):
  number = int(input("digite valor: "))
  lista.append(number)
  if number % 2 == 0:
    pares.append(number)
  if number % 2 == 1:
    impares.append(number)

print("A lista completa: ", lista)
print("A lista de números pares: ",pares)
print("A lista de números ímpares: ", impares)





