n = 0
s = 0
q = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s = s + n
    q = q + 1
print(f'A soma dos {q} valores foi de {s}!')