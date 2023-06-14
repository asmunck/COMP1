# 1. a)
def criar_novo_contato(nome, telefone='', email='', instagram=''):
    """
    Cria um novo contato e retorna uma lista com suas informações.

    nome: O nome do contato (obrigatório).
    telefone: O número de telefone do contato (opcional).
    mail: O email do contato (opcional).
    instagram: O Instagram do contato (opcional).
    return: Uma lista contendo as informações do contato no formato especificado.
    """
    informacoes_contato = [nome, [telefone], email, instagram]
    return informacoes_contato

 # b)
def atualizar_contato(informacoes_contato, indice, nova_informacao):
    """
    Nessa função, a lista informacoes_contato é atualizada diretamente caso a alteração seja permitida (de acordo com as regras especificadas). 
    O valor booleano retornado indica se a alteração foi feita ou não.
    """
    if indice >= 0 and indice < len(informacoes_contato):
        if indice == 0 or indice == 2 or indice == 3:
            informacoes_contato[indice] = nova_informacao
            return True
        elif indice == 1:
            if nova_informacao not in informacoes_contato[indice]:
                informacoes_contato[indice].append(nova_informacao)
                return True
        else:
            return False
    else:
        return False
      
      
      
      
    # 2.
    def traducao_rnaM(rna_mensageiro):
    """
Nessa função, um dicionário tabela_trincas_rna é utilizado para armazenar os mapeamentos entre as trincas de RNA e os aminoácidos correspondentes. 
A função percorre a string rna_mensageiro, a cada 3 caracteres, realiza a tradução utilizando o dicionário e armazena o resultado em uma lista de aminoácidos. 
Por fim, os aminoácidos são concatenados com o separador "-" e retornados como uma única string.
    """
    tabela_trincas_rna = {
        'UUU': 'Phe',
        'CUU': 'Leu',
        'UUA': 'Leu',
        'AAG': 'Lisina',
        'UCU': 'Ser',
        'UAU': 'Tyr',
        'CAA': 'Gln'
    }

    aminoacidos = [tabela_trincas_rna[rna_mensageiro[i:i+3]] for i in range(0, len(rna_mensageiro), 3)]
    return '-'.join(aminoacidos)

