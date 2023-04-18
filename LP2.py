# 1. Defina uma função que retorne o valor de PI importado de Math.
import math
pi = math.pi
print(pi)

# 2. Defina uma função que retorne a potência - Default y = 2
def calcular_potencia(x,y = 2):
  return x ** y

# 3. Defina uma função que calcule a área circular e 4. Função que calcule a coroa circular.
import math
pi = math.pi
def calcular_area_circular(x):
  return pi * (x **2)
def calcular_coroa_circular(r1, r2):
  return calcular_area_circular(r1) - calcular_area_circular(r2)
