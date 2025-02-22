print("Hello, World!")

nome = "Karen"  # String
idade = 25  # Inteiro
altura = 1.68  # Float
ativo = True  # Booleano

print (nome , idade , altura , ativo)

print(type(ativo)) #define o tipo de dados
# <class 'str'> STRING
# <class 'int'> INTERIRO
# <class 'float'> FLOAT 
# <class 'bool'> BOOLEANO

nome = input("Digite seu nome: ")  # Entrada de texto
idade = int(input("Digite sua idade: "))  # Convertendo para inteiro
print(f"Olá, {nome}! Você tem {idade} anos.")  # Interpolação

a, b = 10, 3
print(a + b)    # Soma
print(a - b)    # Subtração 
print( a * b)   # Multiplicação
print(a / b)    # Divisão
print(a // b)   # Divisão Interira 
print(a % b)    # Módulo
print( a ** b)  # Potência

idade = 18
if idade >= 18:
    print("Maior de idade") 
#  # Bloco de código executado se condição1 for verdadeira

elif idade == 17:
    print("Quase lá")
# Bloco de código executado se condição1 for falsa e condição2 for verdadeira

else:
    print("Menor de idade")
 # Bloco de código executado se todas as condições anteriores forem falsas


for i in range(1, 6):
    print(i)
# O FOR é um laço de repetição que percorre valores dentro do intervalo da função range().
# range(1, 6)cria uma sequência de números que começa em 1 e vai até 5(o número 6não está incluído, pois o range()sempre para antes do número final).
# A variável i assume, a cada reprodução, um valor dentro desse intervalo.
# print(i) exibe o valor atual de i na tela a cada iteração.


x = 0
while x < 5:
    print(x)
    x += 1
# loop com while significa "enquanto a condição para verdadeira, continue executando o bloco de código".
# A condição x < 5 é avaliada. Enquanto x for menor que 5, o bloco dentro do while será executado.
# aplicando += 1 é somado +1 a cada repetição

# x = 0, verifica 0 < 5→ Verdadeiro → imprime 0, depois x  soma +1 = 1
# x = 1, verifica 1 < 5→ Verdadeiro → imprime 1, depois x  soma +1 = 2
# x = 2, verifica 2 < 5→ Verdadeiro → imprime 2, depois x  soma +1 = 3.
# x = 3, verifica 3 < 5→ Verdadeiro → imprime 3, depois x  soma +1 = 4.
# x = 4, verifica 4 < 5→ Verdadeiro → imprime 4, depois x  soma +1 = 5.
# x = 5, verifica 5 < 5→ Falso → O loop termina.


frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)
# criamos uma lista chamada frutas contendo três elementos
# for percorre a lista frutas item por item.
# A variável fruta assume, a cada iteração, o valor de um dos elementos da lista.

# fruta = "maçã"→ imprime "maçã".
# fruta = "banana"→ imprime "banana".
# fruta = "uva"→ imprime "uva".
# O loop termina porque não há mais elementos na lista.

numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Primeiro elemento
numeros.append(6)  # Adiciona um item
numeros.remove(3)  # Remove o número 3
# Criamos uma lista chamada numeroscontendo os elementos [1, 2, 3, 4, 5].