
def is_fibonacci(num):
    # Inicializa os primeiros dois números da sequência
    a, b = 0, 1
    
    # Calcula a sequência de Fibonacci até o número informado
    while b < num:
        a, b = b, a + b

    # Verifica se o número está na sequência de Fibonacci
    if b == num or num == 0:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

# Entrada do usuário
numero = int(input("Informe um número para verificar: "))
print(is_fibonacci(numero))
