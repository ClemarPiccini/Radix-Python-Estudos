from pydantic import BaseModel

# Definindo um modelo de dados usando Pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Criando uma instância do modelo e validando os dados
item_data = {"name": "Produto 1", "price": 10.5}
item = Item(**item_data)
print(item.json())

# Tentando criar uma instância com dados inválidos
invalid_item_data = {"name": "Produto 2", "price": "invalid"}
try:
    invalid_item = Item(**invalid_item_data)
except ValueError as e:
    print(f"Erro ao criar o item: {e}")

"""
Neste exemplo, estamos definindo um modelo de dados Item usando o Pydantic, com campos para name (nome do item), price (preço do item) e is_offer (se o item está em oferta). Quando criamos uma instância do Item usando dados válidos, o Pydantic valida automaticamente os dados de entrada conforme as regras definidas no modelo. Se tentarmos criar uma instância com dados inválidos (como um preço inválido), o Pydantic levanta uma exceção informando o problema.

O método json() é usado para serializar um objeto Pydantic em formato JSON, o que pode ser útil ao retornar dados de uma API.
"""