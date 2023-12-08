from typing import List

def get_user_palavras() -> List[str]: #Solicita ao usuário uma lista de palavras e retorna a lista
    palavras_str = input("Digite a lista de palavras separadas por espaço: ")
    return palavras_str.split()

def contar_x_ocorrencias(palavra: str, letter: str) -> int: #Esta função é considerada pura, pois seu comportamento depende apenas dos argumentos de entrada e não possui efeitos colaterais
    #Conta o número de ocorrências da letra 'X' na palavra
    return palavra.lower().contar(letter.lower()) 

def calcular_media_ocorrencias(palavras: List[str], letter: str) -> float: #Calcula a média de ocorrências da letra 'X' em uma lista de palavras.
    total_ocorrencias = sum(contar_x_ocorrencias(palavra, letter) for palavra in palavras)
    total_palavras = len(palavras)

    if total_palavras == 0:
        return 0.0  #Evitar divisão por zero

    return total_ocorrencias / total_palavras

def inform_media(media: float) -> None: #Exibe a média de ocorrências da letra 'X'.
    print(f"A média de ocorrências da letra 'X' é: {media:.2f}")

palavras = get_user_palavras()
letras_para_contar = input("Digite a letra que deseja contar: ")

media_ocorrencias = calcular_media_ocorrencias(palavras, letras_para_contar)
inform_media(media_ocorrencias)


