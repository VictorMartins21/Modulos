def soma_pura(a, b):
    return f"A soma de {a} e {b} é igual a {a + b}."

lista_global = []

def adicionar_item_impuro(item):
    global lista_global
    lista_global.append(f"Novo item: {item}")
    return "Item adicionado com sucesso!"

adicionar_item_impuro("bala")
print(soma_pura(2, 4))
print(lista_global)