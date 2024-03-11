saldo = 1000
saque = 250
limite = 200
conta_especial = True
contatos_emergencia = []

# Operador and: Se todas as expressoes forem verdadeiras, então dá True. Se qualquer uma for falsa, dá False.
exp_and = saldo>= saque and saque >= limite
print(exp_and)

# Operador or: Desde que uma das expressões seja verdadeira, dá True.
exp_or = saldo >= saque or saque <= limite
print(exp_or)

# Operador Negação: Usar not na expressão inverte se é verdadeiro ou falso.
exp_neg_1 = not saldo >= limite
print(exp_neg_1)

# Operador Negação P.S: Strings com conteudo são veradeiras. Listas e string vazias são falsas. Por tanto, o not inverte para False e True respectivamente
exp_neg_2 = not "saque 1500;"
print(exp_neg_2)

exp_neg_3 = not ""
print(exp_neg_3)

exp_neg_4 = not contatos_emergencia
print(exp_neg_4)

# Parenteses (escolhe a precedênica, o que é resolvido primeiro/segmentado)

exp_1 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_1)

conta_normal_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_saldo_suficiente = conta_especial and saldo >= saque

exp_2 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente
print(exp_2)