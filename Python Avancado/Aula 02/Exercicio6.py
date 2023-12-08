def processa_elemento(elemento):

    if isinstance(elemento, int):
        return f"O dobro do número é: {elemento * 2}"
    elif isinstance(elemento, float):
        return f"A metade do número é: {elemento / 2}"
    elif isinstance(elemento, str):
        return f"A string em maiúsculas é: {elemento.upper()}"
    elif isinstance(elemento, list):
        return f"A soma dos elementos da lista é: {sum(elemento)}"
    else:
        return "Tipo de dado não suportado"

resultado_1 = processa_elemento(10)
resultado_2 = processa_elemento(3.5)
resultado_3 = processa_elemento("python")
resultado_4 = processa_elemento([1, 2, 3, 4, 5])

print(resultado_1)
print(resultado_2)
print(resultado_3)
print(resultado_4)
