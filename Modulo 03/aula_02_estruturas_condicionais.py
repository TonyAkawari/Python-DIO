MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe sua idade:"))

# if se  usa como condicional verdadeira
# else se usa como condicional falsa
# elif se usa como uma alternativa ou multiplas alternativas para o if.
"""
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if:
    print("Ainda não pode tirar a CNH.")
"""
"""
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")
"""
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Aulas teóricas sim, aulas práticas não.")

else:
    print("Ainda não pode tirar a CNH.")
