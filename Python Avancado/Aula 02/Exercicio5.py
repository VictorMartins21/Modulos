from typing import Optional

def quadrado_do_numero(numero: Optional[int]) -> str:
    if numero is not None:
        return f"O quadrado do número é: {numero ** 2}"
    else:
        return "Nenhum número fornecido."

resultado_1 = quadrado_do_numero(5)
resultado_2 = quadrado_do_numero(None)

print(resultado_1)
print(resultado_2)
