  #  Função para intercalar elementos de duas listas:
  def intercalar_listas(L1, L2):
    L3 = []
    for i in range(len(L1)):
        L3.append(L1[i])
        L3.append(L2[i])
    return L3

   #   Função para calcular os pontos por time:
    def pontos_por_time(lista_jogos):
    pontos = {}
    for jogo in lista_jogos:
        time1 = jogo[0]
        time2 = jogo[1]
        resultado = jogo[2]
        
        if time1 not in pontos:
            pontos[time1] = 0
        if time2 not in pontos:
            pontos[time2] = 0
            
        if resultado[0] > resultado[1]:
            pontos[time1] += 3
        elif resultado[0] < resultado[1]:
            pontos[time2] += 3
        else:
            pontos[time1] += 1
            pontos[time2] += 1
    
    return pontos

   #   Função para verificar se o colchão passa pelas portas:
    def colchao_passa_pelas_portas(dimensoes_colchao, altura_porta, largura_porta):
    if dimensoes_colchao[0] <= altura_porta and dimensoes_colchao[1] <= largura_porta:
        return True
    elif dimensoes_colchao[0] <= largura_porta and dimensoes_colchao[1] <= altura_porta:
        return True
    else:
        return False

     
