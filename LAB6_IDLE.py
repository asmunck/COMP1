def excluir_telefone(contato, telefone):
    """
    Nessa função, é verificado se o telefone a ser excluído está presente na lista de telefones do contato. 
    Se estiver, ele é removido usando o método remove(). 
    Caso contrário, a função retorna False indicando que nenhuma alteração foi feita. 
    """
    if telefone in contato[1]:
        contato[1].remove(telefone)
        return True
    else:
        return False

      
 def dados_campeonato(tabela):
    """
    Nesse exemplo, a tabela de pontos por time é representada pelo dicionário tabela_pontos. 
    A função dados_campeonato extrai os nomes dos times e as pontuações correspondentes da tabela. 
    Em seguida, calcula a pontuação do time campeão usando a função max() e a média de pontos por time dividindo a soma das pontuações pelo número de times. 
    O resultado é retornado como uma lista contendo os nomes dos times, a pontuação do time campeão e a média de pontos por time.
    """
    times = list(tabela.keys())
    pontuacoes = list(tabela.values())
    pontuacao_campeao = max(pontuacoes)
    media_pontos = sum(pontuacoes) / len(times)
    
    return [times, pontuacao_campeao, media_pontos]
# Exemplo de uso:
tabela_pontos = {
    'Time Flu': 11,
    'Time Fla': 16,
    'Time Bot': 13,
    'Time Vas': 0,
    'Time Mad': 10
}

resultado = dados_campeonato(tabela_pontos)
print(resultado)
