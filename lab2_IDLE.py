# 1.
# a) Funções max e min
max(3, 2.8, 3.9)

min(7, 2, 4, 1, 0)

# b) Função que calcula a média de três números inteiros:
def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# c) Função que retorna a diferença entre o maior número e a média:
def diferenca_maior_media(n1, n2, n3):
    maior = max(n1, n2, n3)
    media = media(n1, n2, n3)
    return maior - media
  
  
# d) Função que retorna a soma do menor número com a média:
def soma_menor_media(n1, n2, n3):
    menor = min(n1, n2, n3)
    media = media(n1, n2, n3)
    return menor + media

  # 2.
# a) Função para calcular o delta
def discriminante(a, b, c):
    return b ** 2 - 4 * a * c
  
# b) Função para calcular a primeira raiz real:
def raiz1(a, b, c):
    delta = discriminante(a, b, c)
    return (-b + delta ** 0.5) / (2 * a)

# c) Função para calcular a segunda raiz real:
def raiz2(a, b, c):
    delta = discriminante(a, b, c)
    return (-b - delta ** 0.5) / (2 * a)

  
  # 3.
# A fórmula para calcular a soma dos n termos de uma PA é Sn = (n/2) * (A1 + An), onde A1 é o primeiro termo, An é o último termo e n é o número de termos.
# Para calcular o número de termos, podemos utilizar a fórmula n = (An - A1)/r + 1, onde r é a razão.
# a) A primeira função, que calcula o número de termos:
def num_termos(A1, An, r):
    n = (An - A1) / r + 1
    return int(n)
# b)
def soma_PA(A1, An, r):
    n = num_termos(A1, An, r)
    soma = (A1 + An) * n / 2
    return soma

   # 4.
# a) Para calcular a distância entre dois pontos em um plano, podemos usar a função "dist" do módulo math:
import math

def distancia_pontos(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))
  
print(distancia_pontos(4, 5, 1, 7)) 
print(distancia_pontos(-4, 3, 5, -2))  
print(distancia_pontos(1, 0, 2, 0)) 

# b) Para calcular o perímetro de um triângulo retângulo dados os catetos, podemos usar a função "hypot" do módulo math:
def perimetro_triangulo(cateto1, cateto2):
    return cateto1 + cateto2 + math.hypot(cateto1, cateto2)

print(perimetro_triangulo(4, 5)) 
print(perimetro_triangulo(7, 14)) 
print(perimetro_triangulo(10, 17))  

# c) Para calcular a soma do quadrado do seno com o quadrado do cosseno de um ângulo, podemos usar as funções "sin" e "cos" do módulo math:
def soma_quadrado_sen_e_cos(angulo):
    return math.sin(angulo)**2 + math.cos(angulo)**2

print(soma_quadrado_sen_e_cos(1)) 
print(soma_quadrado_sen_e_cos(math.pi/3))  
print(soma_quadrado_sen_e_cos(math.pi/3))  


  # 5.
# a) Função para calcular a área de um setor circular da seguinte forma:
def area_setor_circular(raio, angulo=360):
    area_circulo = math.pi * raio**2
    return area_circulo * (angulo/360)
print(area_setor_circular(15)) 
print(area_setor_circular(10, 45)) 
print(area_setor_circular(30, 140))  

