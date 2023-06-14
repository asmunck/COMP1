     #     Função para contar o número de palavras em uma frase:
    def contar_palavras(frase):
    palavras = frase.strip().split()
    return len(palavras)

     #   Função para contar o número de frases em um texto:
    def contar_frases(texto):
    pontuacoes = ['.', '!', '?', '...']
    contador = 0
    for pontuacao in pontuacoes:
        contador += texto.count(pontuacao)
    return contador
 
      #     Função para substituir os caracteres de pontuação por espaços em uma frase:
  def remover_pontuacao(frase):
    pontuacoes = ['-', ',', ':', ';', '.', '!', '?']
    for pontuacao in pontuacoes:
        frase = frase.replace(pontuacao, ' ')
    return frase

      # Função para inverter a ordem das palavras em uma frase, remover letras maiúsculas e pontuação:
    def inverter_frase(frase):
    frase = remover_pontuacao(frase)
    palavras = frase.lower().split()
    palavras.reverse()
    frase_invertida = ' '.join(palavras)
    return frase_invertida

      #     Função para inserir um número em uma lista ordenada mantendo a ordem:
    def insere(lista, numero):
    lista.append(numero)
    lista.sort()

      #     Função para obter os números maiores que um determinado valor em uma lista e ordená-los em ordem crescente:
    def maiores_que(lista, n):
    maiores = [num for num in lista if num > n]
    maiores.sort()
    return maiores
  
      #     Função para obter as notas acima da média em uma lista de notas e ordená-las:
    def acima_da_media(notas):
    media = sum(notas) / len(notas)
    acima_media = [nota for nota in notas if nota > media]
    acima_media.sort()
    return acima_media

