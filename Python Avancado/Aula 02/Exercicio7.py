def duplica_elementos(lista):

    for i in range(len(lista)):
        lista[i] /= 2

numeros = [1, 2, 3, 4, 5]

numeros.append("seis")
duplica_elementos(numeros)

print(numeros)
