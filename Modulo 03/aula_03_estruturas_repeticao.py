# o comando for causa repetição controlada. O for executa uma expressão para cada item determinado
texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print (letra,end=" ")

# O for geralmente é usado sem o else. Raramente é usado com ele.
else:
    print() # print vazio = quebra de linha
    
# Repetição de range. Com ela vai listar do inicio, fim, e step(etapa)[no step se escolhe de qunto em quanto vai contar] os numeros determinados
# Sempre inclui o primeiro numero e esconde o ultimo, planejar de acordo
for numero in range (0, 100, 5):
    print(numero, end=" ")

