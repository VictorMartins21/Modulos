def avaliar_condicao(valor, callback_true, callback_false):
    if bool(valor) and valor >0:
        return callback_true(valor)
    else:
        return callback_false(valor)

def callback_verdadeiro(x):
    return f"Valor {x} é verdadeiro."

def callback_falso(x):
    return f"Valor {x} é falso."

valor_verdadeiro = 5
resultado_verdadeiro = avaliar_condicao(valor_verdadeiro, callback_verdadeiro, callback_falso)
print(resultado_verdadeiro)

valor_falso = 0
resultado_falso = avaliar_condicao(valor_falso, callback_verdadeiro, callback_falso)
print(resultado_falso)
