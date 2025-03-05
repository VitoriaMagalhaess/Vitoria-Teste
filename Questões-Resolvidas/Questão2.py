def pertence_fibonacci(n) :
    a, b = 0, 1

    while b < n:
        a, b = b, a + b
        return b == n or n == 0

def main():
    try:
        num = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
        if pertence_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

if __name__ == "__main__":
    main()








