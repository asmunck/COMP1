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

'''
Questão OBI (Olimpíada Brasileira de Informática - 2009, Fase 1, Nível Júnior) - (Aviões de Papel)

Para descontrair os alunos após as provas da OBI, a diretora da escola organizou um campeonato de aviões de papel. Cada aluno participante receberá uma certa quantidade de folhas de um papel especial para fazer seus modelos de aviões. A quantidade de folhas que cada aluno deverá receber ainda não foi determinada: ela será decidida pelos juízes do campeonato.

A diretora convidou engenheiros da Embraer, uma das mais bem-sucedidas empresas brasileiras que vende aviões com tecnologia brasileira no mundo todo, para atuarem como juízes. O campeonato está programado para começar logo após a prova da OBI, mas os juízes ainda não chegaram à escola. A diretora está aflita, pois comprou uma boa quantidade de folhas de papel especial, mas não sabe se a quantidade comprada vai ser suficiente.

Considere, por exemplo, que a diretora comprou 100 folhas de papel especial, e que há 33 competidores. Se os juízes decidirem que cada competidor tem direito a três folhas de papel, a quantidade comprada pela diretora é suficiente. Mas se os juízes decidirem que cada competidor tem direito a quatro folhas, a quantidade comprada pela diretora não seria suficiente.

Você deve escrever uma função que, dados o número de competidores, o número de folhas de papel especial compradas pela diretora e o número de folhas que cada competidor deve receber, determine se o número de folhas comprado pela diretora é suficiente.

Entrada: Os parâmetros de entrada da função são três números inteiros Competidores, QuantidadePapel e QuantidadeFolhas representando respectivamente o número de competidores, a quantidade de folhas de papel especial compradas pela diretora e a quantidade de folhas de papel especial que cada competidor deve receber.

Saída: A sua função deve retornar "Suficiente" se a quantidade de folhas compradas pela diretora é suficiente, ou "Insuficiente" caso contrário.

Exemplos:
Entrada: 10,100,10 ; Saída: "Suficiente"
Entrada: 10,90,10 ; Saída: "Insuficiente"
Entrada: 5,40,2 ; Saída: "Suficiente"
'''
def suficiente(Competidores, QuantidadePapel, QuantidadeFolhas):
    total_folhas_necessarias = Competidores * QuantidadeFolhas
    
    if total_folhas_necessarias <= QuantidadePapel:
        return "Suficiente"
    else:
        return "Insuficiente"
    
print(suficiente(10, 100, 10))
print(suficiente(10, 90, 10))
print(suficiente(5, 40, 2))
