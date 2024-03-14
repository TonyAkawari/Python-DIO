saldo = 2000
saque = 500
# if ternario permite escrever uma condição em uma unica linha. A estrutura é primeiro o if, a condição, elif (se houver) depois else em ultimo.
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")