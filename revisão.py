# ###Comentário###

variavel = 1

print(variavel)
print(type(variavel))

variavel = '1'

print(variavel)
print(type(variavel))
# Operadores de Atribuição
2 < 4
2 > 4
2 <= 4
2 >= 4
2 == 4
2 != 4

False and True
False or True
not True
# Operadores Aritimeticos
2 + 2
2 - 2
2 * 2
2 / 2
2 % 2 # Resulatado = 0
2 ** 2

(2 + 2) * 2

num1 = 2
num2 = 3

if not ((num1 + num2) > 3):
    print("verdadeiro")
else:
    print ('falso')

if not ((num1 + num2) < 3):
    print("verdadeiro")
else:
    print ('falso')

numTotal = 80

# if numTotal > 80:
#     print('Maior que 80')
#     if numTotal > 70:
#         print ('Maior que 70')
#     else:
#             print('Menor que 70')
if numTotal > 80:
    print('Maior que 80')
elif numTotal > 70:
    print('Maior que 70')
else:
    print('Menor que 70')

import time

segundo = 0

while segundo < 10:
    time.sleep(.500)
    segundo = segundo + 1
    print(segundo)

for rua in range(13):
    print(f'Rua {rua + 1}')

vetor = ["Rua A", "Rua B", "Rua C"]
print(vetor)

for stret in vetor:
    print(stret)
print('\n')
cidade = [
    ["Rua A", "Rua B", "Rua C"],
    ["Rua R", "Rua D", "Rua G"],
    ["Rua U", "Rua J", "Rua Y"],
    ["Rua E", "Rua W", "Rua K"]
]

for bairro in cidade:
    ruasDoBarro = ''
    for rua in bairro:
      ruasDoBarro = ruasDoBarro + rua + "  "
    print(ruasDoBarro)
