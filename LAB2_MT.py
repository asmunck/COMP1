# 1. Pedrinho quer comprar o maior número de bombons possível com o dinheiro que tem. Faça uma função chamada "num_bombons" para calcular quantos bombons ele consegue comprar, dados o dinheiro e o preço do bombom para realização da compra.
# A função avalia se Pedrinho tem dinheiro para comprar algum bombom e quanto ele receberia de troco, caso contrário, recebe uma negativa.
def num_bombons(dinheiro, preco_bombom):
    if dinheiro < preco_bombom:
        return "Pedrinho não pode comprar nenhum bombom."
    else:
        quantidade_bombons = dinheiro // preco_bombom
        troco = dinheiro % preco_bombom
        return (quantidade_bombons, troco)

# 2. Um grupo de amigos deseja fazer uma viagem e decidiram ir de carro. Pelas regras rodoviárias, um veículo convencional tem a capacidade de transportar até 5 passageiros, porém há veículos com outras capacidades. Construa uma função em Python chamada "carros" para calcular e retornar o número exato de carros necessários para esta viagem, considerando que seja dado como entrada o número de pessoas. Caso os veículos considerados sejam de capacidades não convencionais, será dado também como entrada a capacidade dos veículos, considerando que todos os veículos são iguais.
def carros(num_pessoas, capacidade=5):
    num_carros = num_pessoas // capacidade
    if num_pessoas % capacidade != 0:
        num_carros += 1
    return num_carros

# 3. João deseja fazer bolos para seus amigos, usando uma receita que indica que devem ser usadas 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite. Em casa, ele tem A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite. João não tem muita prática com a cozinha, e portanto ele só se arriscará a fazer medidas exatas da receita de bolo (por exemplo, se ele tiver material suficiente para fazer mais do que 2 e menos do que 3 bolos, ele fará somente 2 bolos). Sabendo disto, ajude João escrevendo uma função chamada "bolos" que determine qual a quantidade máxima de bolos que ele consegue fazer.
# Entrada: Os parâmetros de entrada da função são três números inteiros A, B e C, indicando respectivamente o número de xícaras de farinha de trigo, o número de ovos e o número de colheres de sopa de leite que João tem em casa.
# Saída: Sua função deve retornar a quantidade máxima de bolos que João consegue fazer.
  def bolos(A, B, C):
    # Calcula o número máximo de bolos que podem ser feitos
    max_bolos = min(A // 2, B // 3, C // 5)
    return max_bolos
