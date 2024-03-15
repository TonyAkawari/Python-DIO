while True:
    numero = int(input("Informe um numero: "))
    # O break corta a execução de acordo com a determinação (nesse exemplo a execução para ao digitar 10)
    if numero == 10:
        break
    # O continue serve para desviar de algo especifico (nesse exemplo desviar dos numero pares,exibir só ímpares) 
    if numero % 2 == 0:
        continue
    print(numero)
    
""" for numero in range (100):
    if numero % 2 == 0:
        continue
    print (numero, end= " ") """