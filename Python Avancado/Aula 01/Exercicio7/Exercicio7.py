def processar_numeros(numero1, numero2, callback):
    resultado = callback(numero1, numero2)
    return resultado

def somar_numeros(x, y):
    return x + y

def multiplicar_numeros(x, y):
    return x * y

resultado_soma = processar_numeros(3, 4, somar_numeros)
print(f"A soma dos números é: {resultado_soma}")

resultado_multiplicacao = processar_numeros(3, 4, multiplicar_numeros)
print(f"A multiplicação dos números é: {resultado_multiplicacao}")
