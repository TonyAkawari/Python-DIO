nome = "Catdog"
idade = 25
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Catdog", "idade": 25}
# Interpolaçao antiga, nao recomendada
print ("Nome: %s Idade: %d" % (nome, idade))

# Interpolaçao format usando {}
print ("Nome: {} Idade: {} Profissão: {} Linguagem: {} ".format(nome, idade, profissao, linguagem))
print ("Nome: {1} Idade: {0}".format(idade, nome))
print ("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print ("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print ("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

# Esse modo resgata a lista criada chamada dados com o **
print ("Nome: {nome} Idade: {idade}".format(**dados))

# Interpolaçao com f, a mais usada e recomendada
print (f"Nome: {nome} Idade: {idade} Saldo: {saldo}")

# Pode-se alterar espaçamento e numero de caracteres em numeros (aumenta/diminui float até interger)
print (f"Nome: {nome} Idade: {idade} Saldo: {saldo: 0.2f}")
print (f"Nome: {nome} Idade: {idade} Saldo: {saldo: 10.2f}")
print (f"Nome: {nome} Idade: {idade} Saldo: {saldo: 5.1f}")
print (f"Nome: {nome} Idade: {idade: 10.2f} Saldo: {saldo: .0f}")

# Exemplo mais completo
name_1=(input("Seu nome? "))
age_1=(int(input("Sua idade? ")))
prof_1= (input("Qual sua profissão? "))

print (f"Meu nome é {name_1}, tenho {age_1} anos e minha proffisão é {prof_1}!")