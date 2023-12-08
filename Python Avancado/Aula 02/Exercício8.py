dados_compras = [
    {"tipo": "produto", "nome": "Camiseta", "preco": 25.99},
    {"tipo": "servico", "nome": "Limpeza", "preco": 50.00},
    {"tipo": "produto", "nome": "Tênis", "preco": 89.99},
    {"tipo": "produto", "nome": "Livro", "preco": 19.99},
    {"tipo": "servico", "nome": "Manutenção", "preco": 120.00},
]

total_compras = 0.0

for compra in dados_compras:
    if isinstance(compra, dict) and "preco" in compra:
        total_compras += compra["preco"]
        print(f"{compra['tipo'].capitalize()}: {compra['nome']} - Preço: R${compra['preco']:.2f}")

print(f"\nTotal de compras: R${total_compras:.2f}")
