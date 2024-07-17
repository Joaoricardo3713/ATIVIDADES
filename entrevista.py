# Uma entrevistadora precisa de um programa para analisar os dados etários
# de grupos de entrevistados.
# Ela solicita a criação de um programa que 
# leia a idade de 10 pessoas, e mostre no final :

# a) Qual é a média de idade do grupo
# b) Quantas pessoas são maiores de idade
# c) Quantas são menores de idade
# d) Qual foi a maior idade lida

somaIdade = 0
maioridade = 0
menoridade = 0 
idademaior = 0
numpessoa = 0
opcao = 0
  
while opcao != 'n':
    for numpessoa in range(1,11,1):
        Idade = + int(input(f"idade pessoa {numpessoa}:"))
    somaIdade = somaIdade + Idade
    if (Idade >=18):
        maiordade = maiordade + 1
    else:
        menoridade = menoridade + 1
    if Idade>idademaior:
        idademaior = Idade

        mediaidade = somaIdade/10

        opcao = input('deseja continuar (s/n)')

print('media de idade ',mediaidade)
print(f'maiores de idade{maioridade} pessoas')
print(f'menor de idade: {menoridade} pessoas')

