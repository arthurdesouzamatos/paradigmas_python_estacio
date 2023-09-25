#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
lista = []
vogais = ["b", "d", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"]


for x in range (10):
  caractere = input("digite um caractere: ")
  if any(caractere.lower() == l for l in vogais):
    lista.append(caractere)

print(lista)
