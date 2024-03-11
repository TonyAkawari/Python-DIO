# Identação básica: Quando se colocar : o VSCode regista ja como bloco e da 4 epaços de identação (1 Tab)

def sacar(valor):
    saldo = 500
    
    if saldo >= valor: #Com o operador if, essas mensagens só aparecem se for True
        print("valor sacado!")
        print("Retire seu dinheiro")
    
    print("Obrigado por ser noso cliente, tenha um bom dia.") #Como a indetação está fora do if, essa mensagem aaparece mesmo se o if for False
        



def depositar(valor):
    saldo = 500
    saldo += valor
    
    if saldo >= valor:
        print("Seu saldo atual é", saldo)
    
sacar(100)
depositar(1000)