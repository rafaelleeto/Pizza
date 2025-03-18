import os
import titulo
import cadastrar
import alterar

while True:
    titulo.titulo()
    print("\n")
    print("1-Cadastrar Pizza\n2-Listar Pizzas\n3-Alterar pedido\n4-Sair")
    opcao=int(input("Bem vindo ao menu da casa, selecione uma opção!"))
    
    if opcao==1:
        cadastrar.Cadastro()
    
    elif opcao==2:
        listar()
        
    elif opcao==3:
        alterar()
    
    elif opcao==4:
        break
        
    else:
        print("Algo deu errado, tente novamente")
        
        
    
    