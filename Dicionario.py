pessoa = {
    "CPF" : "123456789012",
    "Nome" : "Fernando",
    "DataNascimento" : "10/10/1910"
}

# print (pessoa)

# print(pessoa["CPF"])

# print(pessoa["DataNascimento"])

pessoa["Nome"] = "Fernando Passos"

# print (pessoa)

pessoa["DataEmissão"] = "02/02/2002"
# print (pessoa)

usuario = {}

usuario ["NomeUsuario"] = "Fernando"
usuario ["Senha"] = "123"
usuario ["NomeCompleto"] = "Fernando Passos"
usuario ["DataDeRegistro"] = "10/10/2010"

# # print(usuario)

# u = input("Digite seu nome de usuário:   ")
# s = input("Digite sua Senha:  ")

# if(usuario["NomeUsuario"] == u and usuario["Senha"] == s):
#     print("Bem vindo ao sistema X!")
# else:
#     print("Usuário ou senha invalido!")

for chave in usuario:
    # print(chave)
    # print (f"chave: {chave} - Valor: {usuario[chave]}")
    pass


leitores =[ 
    {
        "nome" : "Fulano",
        "identidade" : "0987654",
        "livros" : ["1808", "1822"],
        "atrasado" : True
    },
    {
        "nome" : "Beltrano",
        "identidade" : "0987654",
        "livros" : ["Dante", "Mitologia"],
        "atrasado" : True
    },
    {
        "nome" : "Sicrano",
        "identidade" : "0987654",
        "livros" : ["Mar de Mostros", "Labirinto do Minotauro"],
        "atrasado" : False
    },
    {
        "nome" : "Wally",
        "identidade" : "0987654",
        "livros" : ["O Hobbit", "O Senho dos Anéis"],
        "atrasado" : True
    }
]


print(leitores)

for leitor in leitores:
    for chave in leitor:
        print(chave, leitor[chave])

# for livros in leitores["livros"]:
#     # print(f"Nome do leitor:  {leitor['nome']} - Nome do livro:  {livros}")
    pass