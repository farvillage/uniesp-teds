palavra = input("Digite uma palavra: ")

palavra_invertida = ""
for letra in palavra:
    palavra_invertida = letra + palavra_invertida

if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")