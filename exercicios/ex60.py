'''from math import factorial
n = int(input('Digite um número para ver o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')''' #com biblioteca math do python
n = int(input('Digite um número para ver o seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}') #sem a biblioteca math do python