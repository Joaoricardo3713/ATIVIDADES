politica = int(input("digite a sua data de nascimento"))
resultado =int(2024-politica)


if resultado <16:
    print("maioridade: menor de idade")
    print("votar: não permitdo")
    print("dirigir: não pode")

if resultado <18:
    print("maioridade: menor de idade")
    print("votar: facultativo")
    print("dirigir: não pode")

if resultado>=16 and resultado<18:
    print("maioridade: menor de idade")
    print("votar: facultativo")
    print("dirigir: não pode")



if resultado>=18 and resultado<70:
    print("maioridade: maior de idade")
    print("votar: obrigatorio")
    print("dirigir: pode dirigir")

if resultado>=70:
    print("maioridade: maior de idade")
    print("facultativo")
    print("dirigir: pode dirigir")

    
