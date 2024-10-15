# 1) Fibonacci

def fibonacci_check(num):
    a, b = 0, 1
    fib_sequence = [a, b]
    
    while b < num:  # enquanto o último número na sequência for menor que o número informado
        a, b = b, a + b  # atualiza a e b
        fib_sequence.append(b)  # adiciona o novo número à sequência
    
    # Verifica se o número tá na sequência
    if num in fib_sequence:
        return f"Uhuu! {num} tá na sequência de Fibonacci! 🚀"
    else:
        return f"Ops! {num} não faz parte da sequência de Fibonacci. 😢"

# Vamos testar com um número
print(fibonacci_check(21))  # Tenta com 21

# 2) Contar 'a' na string

def contar_a(string):
    count = string.lower().count('a')  # conta quantas vezes 'a' aparece
    return f"A letra 'a' aparece {count} vezes na string."

# Testando com uma string
print(contar_a("Aprendendo Python é bem legal!"))

# 3) Lógica do código
# O código calcula a soma dos números de 1 até 12 (12 - 1).
# No final, SOMA será 78.

soma_valor = 0
indice = 12
k = 1

while k < indice:  # enquanto k for menor que 12
    k += 1  # k vai subindo
    soma_valor += k  # soma os valores

# Resultado da soma
print(f"Após a execução, a variável SOMA é {soma_valor}.")

# 4) Próximos elementos
# a) 1, 3, 5, 7, ___ -> 9 (números ímpares)
# b) 2, 4, 8, 16, 32, 64, ____ -> 128 (dobrando)
# c) 0, 1, 4, 9, 16, 25, 36, ____ -> 49 (quadrados perfeitos: 7²)
# d) 4, 16, 36, 64, ____ -> 100 (quadrados perfeitos: 10²)
# e) 1, 1, 2, 3, 5, 8, ____ -> 13 (Fibonacci)
# f) 2, 10, 12, 16, 17, 18, 19, ____ -> 20 (contagem até 20)

# 5) Interruptores e lâmpadas
# Aqui tá a estratégia:
# 1. Liga o primeiro interruptor e espera uns 5 minutos. Desliga ele.
# 2. Liga o segundo interruptor.
# 3. Corre até as lâmpadas:
# - Se a lâmpada tá acesa, é do segundo interruptor.
# - Se tá apagada e quente, é do primeiro.
# - Se tá apagada e fria, é do terceiro.
