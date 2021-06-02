print ("Bem-Vindo Ao Predio Tofu")



Andares = int(input("Digite o numero de Andares que deseja?  "))

Apartamentos = int(input("Digite o Número de Apartamento que deseja?  "))

def incremento (numero):
    numero = numero + 1
    return numero

num = incremento(Apartamentos)

print(num)

print(incremento(Apartamentos))

import time

for Andares in range (Andares,  -1, -1):
    print(Andares)
    print(f"{int(Andares)}  Andar ")

    for Apartamentos in range (Apartamentos, -1, -1):
        print(Apartamentos)
        print(f"Ap {int(Apartamentos)}")

        time.sleep (0.8)

print ("See you!!!")