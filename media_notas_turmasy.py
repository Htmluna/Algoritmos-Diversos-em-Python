#Função para solicitar notas dos alunos
def solicitar_notas(tipo, intervalo):
    notas = []
    print(f"Você está digitando as notas dos 25 primeiros alunos {tipo}.")
    for i in intervalo:
        while True:
            try:
                nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Insira uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    return notas

# Solicitar as notas dos alunos ímpares
notas_impares = solicitar_notas("ímpares", range(1, 50, 2))

# Solicitar as notas dos alunos pares
notas_pares = solicitar_notas("pares", range(2, 51, 2))

# Calcular as médias
media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

# Exibir as médias
print(f"Média das notas dos alunos ímpares: {media_impares:.2f}")
print(f"Média das notas dos alunos pares: {media_pares:.2f}")

# Determinar qual metade teve a maior média
if media_impares > media_pares:
    print("A metade dos alunos ímpares teve a maior média.")
elif media_pares > media_impares:
    print("A metade dos alunos pares teve a maior média.")
else:
    print("As duas metades tiveram médias iguais.")
