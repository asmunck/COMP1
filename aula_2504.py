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
