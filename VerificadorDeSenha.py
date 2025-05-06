### PROGRAMA VERIFICADOR DE SENHAS FORTES ###

from random import randint as ran
from random import shuffle


def Verificador_de_Senha(pedidoSenha):

    caracter=['@','$','#','!','%','*']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z']
    letras_minusculas = [letra.lower() for letra in letras]
    senha = list(pedidoSenha)
    
   # print(senha)
    
    
    if len(senha)==6:
        
        contador = cont = aux = var = 0
        for i in range(0,6):
            if senha[i] in numeros:
                contador +=1

            elif senha[i] in caracter:
                aux +=1

            elif senha[i] in letras:
                cont +=1

            elif senha[i] in letras_minusculas:
                var +=1


        if contador != 3 or aux!= 1 or cont !=1 or var != 1 :
            print('SUA SENHA NÃO ESTÁ NO PADRÃO PEDIDO, TENTE NOVAMENTE!')
            

            sugestao_de_senha(caracter,numeros,letras,letras_minusculas)
            
            
            Entrada_do_Usuario()

        else:
            print('ok')
            
            
            
                  
            

    else:
        print('Quantidade de caracteres diferente de 6 , tente novamente')

        sugestao_de_senha(caracter,numeros,letras,letras_minusculas)
        
        Entrada_do_Usuario()

        

def sugestao_de_senha(caracter,numeros,letras,letras_minusculas):


    i = ran(0,5)
    j=ran(0,25)
    x = ran(0,25)

    
    
  
    print('SUGESTÃO: ',caracter[i],letras[j],letras_minusculas[x],ran(0,9),ran(0,9),ran(0,9))

    

    
    



def Entrada_do_Usuario(*n):
    

    pedidoSenha = input('Digite uma senha que contenha: 3 números,1 Caracter especial, 1 letra Maiúscula e 1 Minúscula ')
    
    
    Verificador_de_Senha(pedidoSenha)
    
    
    
print(Entrada_do_Usuario())
