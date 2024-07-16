# Inicializar uma lista para armazenar os votos
votos = [0, 0, 0, 0, 0]

# Solicitar a quantidade de votos para cada dia da semana
for i in range(5):
    votos[i] = int(input(f"Digite a quantidade de votos para {['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira'][i]}: "))

# Encontrar o dia com mais votos
dia_escolhido = votos.index(max(votos))
print(f"O dia escolhido para as lives é {['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira'][dia_escolhido]}.")
