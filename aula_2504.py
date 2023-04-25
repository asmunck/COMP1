# 1.
def habilitacao(idade, pratica, teorica):
  if idade < 18:
    print("Inapto por idade.")
  elif pratica == False:
    print("Inapto na prática.")
  elif teorica == False:
    print("Inapto na teórica.")
  else:
    print("Aprovado.")

habilitacao(18, True, False)

# 2.
def trianguloisosceles(lado1, lado2, lado3):
  if lado1 == lado2 and lado3 != lado1:
    print("Triângulo isosceles")
  else:
    print("Triângulo não isosceles.")
