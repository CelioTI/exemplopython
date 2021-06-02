# predio = [
#     ["Ap 100", "Ap 101", "Ap 102", "Ap 103"],
#     ["Ap 200", "Ap 201", "Ap 202", "Ap 203"],
#     ["Ap 300", "Ap 301", "Ap 302", "Ap 303"],
#     ["Ap 400", "Ap 401", "Ap 402", "Ap 403"]
# ]

# for andar in predio:
#     print(andar)

predio = []

andares = int(input("Qual a quantidade de andares?  "))
apartamentosporandar = int(input("Qual a quantidade de apartamento por andares?  "))

for i in range(andares):
    andar = []
    for j in range(apartamentosporandar):
        andar.append(f"Apto {i+1}0{j+1}")
    predio.append(andar)
for i in range(andares, 0, -1):
    print(predio[i-1])   

for i in range(len(predio), 0 , -1):
    print(predio[i-1])