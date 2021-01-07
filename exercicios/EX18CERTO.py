from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))

