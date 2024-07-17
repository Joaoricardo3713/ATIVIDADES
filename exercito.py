



#O exercito te contratou para criar um programa que mostre aos brasileiros a situação deles em relação ao serviço militar.
# - Em tempos de paz, a Partir dos 17 anos qualquer brasileiro pode se alistar como voluntário
#    - Em tempos de paz a convocação pode ocorrer no dia primeiro de janeiro do ano em que a pessoa completa 18 anos de idade até 31 de dezembro do ano em que a pessoa completa 45 anos
#    - Em tempos de guerra qualquer brasileiro pode ser convocado a partir dos 17 anos.

# A partir dos dados acima crie um programa que mostre de forma clara em qual situação uma pessoa se encontra. 
#O exercito solicitou que mesmo que alguém não esteja em idade de alistamento, seja informado em que ano o alistamento deve ocorrer.

idade = int(input("sejá bem vindo ao exercito brasileiro  por favor, digite sua idade!:"))

minima = (18)-(idade)

tempo = input("digite o tempo em que estamos,(estamos em guerra)? ")

if (idade <17) and (tempo == 'nao'):
    print(f"você brasileiro ainda não pode ser convocado mas pode se alistar como voluntário, falta {minima} anos, aguardamos ansioso por você\n..................................")
if (idade <17) or (idade>45) and (tempo == 'nao'):
    print (f"voce não pode ser convocado, nem se alistar como voluntario.\n.......................")
elif (idade <18)and (tempo == 'nao'): 
    print(f" você brasileiro pode se alistar como voluntário\n...........................")
else:
    print("voce é obrigado a se alistar e você pode ser convocado\n..............................")
    

   
if (idade <17) or (idade>45) and (tempo =='sim'):
    print (f"voce não pode ser convocado")
if (idade >=17 or (idade<=45)) and (tempo =='sim'):
    print("você foi convocado")

















