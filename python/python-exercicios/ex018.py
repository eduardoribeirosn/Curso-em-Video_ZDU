from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {} tem o Seno de {:.2f}' .format(angulo, sen))
print('O ângulo de {} tem o Cosseno de {:.2f}' .format(angulo, cos))
print('O ângulo de {} tem o Tangente de {:.2f}' .format(angulo, tan))