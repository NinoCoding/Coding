/*Você vai ao mercado fazer compras para a semana e precisa atualizar a sua lista. Agora,
precisa atualizar a lista corretamente. Você precisa retirar o Cereal e incluir Frango e Carne
Lista de compras:
- Arroz
- Feijão
- Leite
- Ovos
- Cereal*/

var listaCompras: [String] = ["Arroz", "Feijao", "Leite", "Ovos", "Cereal"]

print("Lista de compras desatualizada: ", listaCompras)
listaCompras.remove(at: 4)
listaCompras.append("Frango")
listaCompras.append("Carne")
print("Lista de compras atualizada: ", listaCompras)