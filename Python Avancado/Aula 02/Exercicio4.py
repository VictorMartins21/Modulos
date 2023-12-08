from typing import List

class Animal:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

def todos_sao_mamiferos(animais: List[Animal]) -> bool:
#    Verifica se todos os animais na lista são mamíferos

 #   Args:
    #animais (List[Animal]): Lista de objetos do tipo Animal

 #   Returns:
    #bool: True se todos os animais são mamíferos, False caso contrário
    for animal in animais:
        if not isinstance(animal, Animal) or animal.tipo != "mamífero":
            return False
    return True

lista_animais = [
    Animal("Cachorro", "mamífero"),
    Animal("Gato", "mamífero"),
    Animal("Pássaro", "ave"),  # Erro animal nao mamifero
]

resultado = todos_sao_mamiferos(lista_animais)
print(f"Todos os animais são mamíferos? {resultado}")
