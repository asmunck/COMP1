def idade_camila(idade_cibele, idade_celeste, idade_camila):
    # Verifica a condição: Cibele nasceu antes de Camila
    if idade_cibele < idade_camila:
        # Verifica a condição: Celeste nasceu depois de Camila
        if idade_celeste > idade_camila:
            return idade_camila
    # Se as condições não forem satisfeitas, retorna None
    return None

  
  def idade_camila(idade_cibele, idade_celeste, idade_camila):
    # Verifica se as idades estão dentro das restrições
    if 5 <= idade_cibele <= 100 and 5 <= idade_celeste <= 100 and 5 <= idade_camila <= 100:
        # Verifica a condição: Cibele nasceu antes de Camila
        if idade_cibele < idade_camila:
            # Verifica a condição: Celeste nasceu depois de Camila
            if idade_celeste > idade_camila:
                return idade_camila
    # Se as condições não forem satisfeitas, retorna None
    return None
