import os 

pizzas_vendidas=[{}]

pizzas=[{"Nome":"Portuguesa","Ingredientes":"Queijo,Massa de tomate,Cebola","Vendida":False},
        {"Nome":"Margherita","Ingredientes":"Queijo,Massa de tomate,Basilico","Vendida":False},
        {"Nome":"Peperoni","Ingredientes":"Queijo,Massa de tomate,Peperoni","Vendida":False},
        {"Nome":"Calabresa","Ingredientes":"Queijo,Massa de tomate,Calabresa","Vendida":False}
        ]

def Cadastro():
    print("\n1-Portuguesa\n-2Margherita\n3-Peperoni\n4-Calabresa\n5-Sair")
    opcao = int(input("Selecione qual pizza você deseja selecionar!"))
    
    if opcao==1:
        nova_pizza = {"Nome":"QuatroQueijos","Ingredientes":"Queijo, Queijo Mussarela, Massa de tomate,Cebola","Vendida":True}
        pizzas.append(nova_pizza)
        print(pizzas)
    
    if opcao==2:
        pizzas.append("Margherita","Queijo,Massa de tomate,Basilico",False)
        print(pizzas)

        

        
