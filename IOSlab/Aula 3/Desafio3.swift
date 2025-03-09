/*Você está desenvolvendo um jogo de RPG e ficou responsável por criar um sistema de classificação
de personagens. Cada classe de personagem tem atributos únicos, como vida e ataque. Seu objetivo
é armazenar essas informações e exibi-las corretamente.
O jogo possui 3 classes de personagem: Guerreiro, Mago e Arqueiro. Os atributos únicos são os
seguintes:
Guerreiro: Vida 150, Ataque 50
Mago: Vida 80, Ataque 100
Arqueiro: Vida 100, Ataque 75
Exiba as classes de personagens com seus respectivos atributos utilizando Dictionary e Tuple*/

let mago = ("Mago", 80, 100)
let guerreiro = ("Guerreiro", 150, 50)
let arqueiro = ("Arqueiro", 100, 75)

print(mago.0, ": Vida", mago.1, ", Ataque", mago.2)
print(guerreiro.0, ": Vida", guerreiro.1, ", Ataque", guerreiro.2)
print(arqueiro.0, ": Vida", arqueiro.1, ", Ataque", arqueiro.2)

/*var personagens: [String: (vida: Int, ataque: Int)] = [
    "Mago": (80, 100),
    "Guerreiro": (150, 50),
    "Arqueiro": (100, 75)
]

// Acessando os valores
print("O Guerreiro tem \(personagens["Guerreiro"]!.vida) de vida e \(personagens["Guerreiro"]!.ataque) de ataque.")

// Modificando os valores
personagens["Mago"]?.vida += 10
print("Nova vida do Mago: \(personagens["Mago"]!.vida)")
*/