politica = int(input("digite a sua data de nascimento"))
resultado =int(2024-politica)

print('idade: ',resultado)

if resultado>=18:
    print('maioridade: maior de idade')
    print('pode dirigir')
else:
    print('maioridade: menor de idade')
    print('nao pode dirigr')


    if resultado<16:
        print('votar: não permitido')
    else:
        if (resultado<18) or (resultado>70):
            print('votar: facultativo')
        else:
            print( 'votar: obrigatorio')