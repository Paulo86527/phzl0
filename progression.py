import json


# Carrega os dados de progressão
with open("progression.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# Pega o XP atual
xp = data["player"]["xp"]


# Tabela de níveis
levels = [
    (1, 0, "Beginner"),
    (2, 1000, "Apprentice"),
    (3, 2500, "Apprentice"),
    (4, 4500, "Developer"),
    (5, 7000, "Developer"),
    (6, 10000, "Developer"),
    (7, 14000, "Advanced Developer"),
    (8, 18000, "Advanced Developer"),
    (9, 23000, "Advanced Developer"),
    (10, 28000, "System Builder"),
]


# Descobre o maior nível alcançado
current_level = 1
current_rank = "Beginner"

for level, required_xp, rank in levels:
    if xp >= required_xp:
        current_level = level
        current_rank = rank


# Mostra o resultado
print("🎮 DEVELOPER PROGRESSION")
print("-------------------------")
print(f"XP: {xp}")
print(f"Level: {current_level}")
print(f"Rank: {current_rank}")
