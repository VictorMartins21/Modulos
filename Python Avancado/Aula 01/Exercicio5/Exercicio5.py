def executar_operacao(numero, callback):
    resultado = callback(numero)
    return resultado

def calcular_quadrado(x):
    return x ** 2

def calcular_inverso(x):
    if x != 0:
        return 1 / x
    else:
        return "Impossível calcular o inverso de zero."

numero_exemplo = 5
resultado_quadrado = executar_operacao(numero_exemplo, calcular_quadrado)
print(f"Quadrado de {numero_exemplo}: {resultado_quadrado}")

numero_exemplo = 2
resultado_inverso = executar_operacao(numero_exemplo, calcular_inverso)
print(f"Inverso de {numero_exemplo}: {resultado_inverso}")
