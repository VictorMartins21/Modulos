from typing import Union

def concatena_strings(a: str, b: str, c: Union[str, None]) -> str:
    resultado = a + b

    if c is not None:
        resultado += c

    return resultado

resultado_1 = concatena_strings("Olá", " ", "Mundo")
resultado_2 = concatena_strings("Python", " é ", None)

print(resultado_1)
print(resultado_2)
