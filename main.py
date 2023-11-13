
#Soma de dois números:

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print(type(n1))
print(f"A soma de {n1} + {n2} é =  {soma}")

print(1 * '\n')
print("-------------------------")

#Sucessor e Antecessor:

numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero +1
print(f"O sucessor do número {numero} é {sucessor} e o antecessor é {antecessor}")

print(1 * '\n')
print("-------------------------")

#Dobro/ triplo/ raiz quadrada:
numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f"O dobro de {numero} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz}")

print(1 * '\n')
print("-------------------------")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média entre {nota1} e {nota2} é {media}.")

print(1 * '\n')
print("-------------------------")

medida = float(input("Digite uma medida em metros: "))
cm = medida * 100
mm = medida * 1000
print(f"{medida} m em centímetros é {cm} cm e em milímetros é {mm} mm.")

print(1 * '\n')
print("-------------------------")

tabuada = int(input("Digite um número para ver a tabuada: "))
for c in range(1, 11):
    print(f"{tabuada} x {c} = {tabuada * c}")

print(1 * '\n')
print("-------------------------")

real = float(input("Digite um valor em reais: "))
dolar = real / 4.95
print(f"O valor de {real} reais em dólares é {dolar}.")
