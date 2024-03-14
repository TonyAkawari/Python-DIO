# Conta
normal = True
universitaria = False
especial = False

saldo = 2000
saque = int(input("Quanto de saque?"))
cheque_especial = 450

# if aninhado é justamente if/elif e else dentro deles mesmos. Condiçoes dentro de condiçoes.
if normal:
    if saldo > saque:
        print("Saque realizado com sucesso!")
    elif saque == saque:
        print("Saque realizado! Sua conta está zerada.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!")
    else:
        print("Não foi possível realziar o saque, saldo insuficiente!")
    
elif universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
        
elif especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")