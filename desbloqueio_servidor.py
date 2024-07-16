def calcular_fatorial(n):
    """Função para calcular o fatorial de um número."""
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def solicitar_minutos():
    """Função para solicitar os minutos atuais com verificação de entrada."""
    while True:
        try:
            minutos = int(input("Digite os minutos atuais (0-59): "))
            if 0 <= minutos <= 59:
                return minutos
            else:
                print("Entrada inválida. Por favor, insira um número entre 0 e 59.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# Solicitar os minutos atuais
minutos = solicitar_minutos()

# Calcular o fatorial
fatorial = calcular_fatorial(minutos)

# Construir a senha
senha = "LIBERDADE" + str(fatorial)

# Exibir a senha
print("A senha necessária para desbloqueio é:", senha)
