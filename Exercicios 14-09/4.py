#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
lista = []
contador = 0;


while contador < 4:
  number = int(input("Informe a nota: "))
  contador += 1
  lista.append(number)

soma = sum(lista)
media = soma/len(lista)
print("As notas são: ", lista)
print('A média é %.2f' % (media))


