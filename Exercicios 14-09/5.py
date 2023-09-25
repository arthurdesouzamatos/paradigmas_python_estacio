#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
notas = []
medias = []
contador = 0

while contador <= 10:
  for x in range (4):
    number = int(input("Informe a nota: "))
    notas.append(number)

  soma = sum(notas)
  media = soma/len(notas)
  contador += 1

  if media >= 7:
    medias.append(media);
  notas.clear()
  alunos_na_media = len(medias)
  print(medias)
  print("número de alunos com nota maior ou igual a 7: ", alunos_na_media)
