from random import choice

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))

lista = [n1,n2,n3,n4]

aleatorio = choice(lista)

print ("*"*20, "NOME SORTEADO", "*"*20)
print ("")

if aleatorio == n1:
    print ("O nome sorteado foi:", n1)
elif aleatorio == n2:
    print ("O nome sorteado foi:", n2)
elif aleatorio == n3:
    print ("O nome sorteado foi:", n3)
elif aleatorio == n4:
    print ("O nome sorteado foi:", n4)


tamanho = len(lista)
print (tamanho)