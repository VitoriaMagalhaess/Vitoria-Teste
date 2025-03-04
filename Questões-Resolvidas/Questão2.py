```
def pertence_fibonacci(n) :
    a, b = 0, 1

    while b < n:
        a, b = b, a + b
        return b == n or n == 0

num = int(input("Digite um número para verificar se está funcionando na sequência de Fibonacci: "))
if pertence_fibonoacci(num) :
print(f"O número {num} pertence a sequência Fibonacci.") 
else:
    print(f"O número {num} não pertence a sequência Fibonacci.")
```   
