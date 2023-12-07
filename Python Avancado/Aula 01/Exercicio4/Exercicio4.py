def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    print(f"Função impura: Elemento '{elemento}' adicionado à lista.")

lista_original = [1, 2, 3]
print(f"Lista original antes da função: {lista_original}")

adicionar_elemento(lista_original, 4)

print(f"Lista original após a função: {lista_original}")
