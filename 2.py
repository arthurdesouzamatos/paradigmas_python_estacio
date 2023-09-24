#Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
lista = []

for x in range (10):
  a = int(input("digite valor: "))
  lista.append(a)
print(list(reversed(lista)))
