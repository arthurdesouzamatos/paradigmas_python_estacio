letras = ["s","c","v","d"]
while True:
  frase = input("Seu estado civil (s, c, v, d): ")
  if any(frase.lower() == l for l in letras):
    break
  else:
    print("Estado civil inválido")