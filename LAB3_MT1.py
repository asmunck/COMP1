'''
Questão OBI (Olimpíada Brasileira de Informática - 2012, Fase 1, Nível Júnior) - (Campeonato)
Dois times, Flamengo e Corinthians, participam de um campeonato de futebol, juntamente com outros times. Cada vitória conta três pontos, cada empate um ponto. Fica melhor classificado no campeonato um time que tenha mais pontos. Em caso de empate no número de pontos, fica melhor classificado o time que tiver maior saldo de gols. Se o número de pontos e o saldo de gols forem os mesmos para os dois times então os dois times estão empatados no campeonato. Dados os números de vitórias e empates, e os saldos de gols dos dois times, sua tarefa é determinar qual dos dois está melhor classificado, ou se eles estão empatados no campeonato.

Entrada: Os parâmetros de entrada da função são seis números inteiros C, Ce, Cs, Fv, Fe e Fs, que são, respectivamente, o número de vitórias do Flamengo, o número de empates do Flamengo, o saldo de gols do Flamengo, o número de vitórias do Corinthians, o número de empates do Corinthians e o saldo de gols do Corinthians.

Saída: A sua função deve retornar 'Flamengo', se Flamengo é melhor classificado que Corinthians; 'Corinthians', se Corinthians é melhor classificado que Flamengo; e se os dois times estão empatados a função deve retornar 'Empate'.
'''
def melhor_classificado(C, Ce, Cs, Fv, Fe, Fs):
    pontos_flamengo = C * 3 + Ce
    pontos_corinthians = Fv * 3 + Fe
    if pontos_flamengo > pontos_corinthians:
        return 'Flamengo'
    elif pontos_corinthians > pontos_flamengo:
        return 'Corinthians'
    else:
        if Cs > Fs:
            return 'Flamengo'
        elif Fs > Cs:
            return 'Corinthians'
        else:
            return 'Empate'
          
print(melhor_classificado(10,5,18,11,2,18))
print(melhor_classificado(10,5,18,11,1,18))
print(melhor_classificado(9,5,-1,10,2,10))
