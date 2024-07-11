# oque é uma condição ?
# as expressoes usam operadores logicos 
#== > >= < <= !=
ana = ['ana das dores',24,'f',1.20]
idade = ana[1]
altura = ana[3]
print(" ana é maior de idade : ", idade>=18)

# pode brincar na montanha russa pessoas com menos de 1.20
altura = ana[3]
print('pode ir na montanha russa :', ana[3]< 1.20)

print("porta abriu : ",ana[0] == ' joao alfredo') 

print ('pode brincar : ' ,(idade>=18) and (altura <1.20))      

# pode entrar na boate 
joao = ['joao feliz', 18, True]
maria = ['maria das dores' ,23,False]
anderson = ['anderson da silva' ,17,True]

print("entra na balada : ",(joao[1] >=18) or (joao[2]==True))
