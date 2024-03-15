curso = "   Python  "
name = "Catdog"

# Letra maiuscula, minuscula e capitalizada respectivamente.
print(name.upper())
print(name.lower())
print(name.title())

# Remove espaços em branco
print(curso.strip())

# Remove espaços em branco da esquerda
# O +"."é pra ajudar na visualização
print(curso.lstrip() +".")

# Remove espaços em branco da direita
print(curso.rstrip() +".")

# .center centraliza e há 2 argumentos no fim: Numero de caracteres pra alterar, e qual caractere vai usar nisso.
print(name.center(20,"#"))

# Forma bruta de fazer semelhente á cima
print("###" + name + "###")

# .join coloca um determinado valor em cada letra. Espaços, pontuação, etc.
print(".".join(name))

words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)