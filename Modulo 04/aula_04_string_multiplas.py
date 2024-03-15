nome = "Severino"

# Pode-se usar strings que seriam inutilizades em blocos de texto com recuo
mensagem = f"""
    Olá, meu nome é {nome}.
Eu estou aprendendo Pyhon.
        Essa mensagem tem recuos.
"""
print (mensagem)

print(
    """  
    ==== MENU ====
    
    
    1 - Depositar
        2 - Sacar
            0 - Sair
    
    ==============

            Obrigado pela preferencia!
    """
)

# Forma bruta de replicar a formataçao de cima

menu = "==== Menu ====\n"
menu += "\n"
menu += "1 - Depositar\n"
print(menu)