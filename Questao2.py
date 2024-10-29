def count_a_in_string(string):
    # Converte para minúsculas e conta ocorrências de 'a'
    count = string.lower().count('a')
    
    # Verifica a presença e retorna o resultado
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não está presente na string."

# Entrada do usuário ou string pré-definida
string = input("Informe uma string para verificar (ou pressione Enter para usar a string padrão): ")

# String padrão, caso o usuário não insira nada
if not string:
    string = "Exemplo padrão para contagem de letras"

# Resultado
print(count_a_in_string(string))
