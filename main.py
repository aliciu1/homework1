class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


hero1 = Hero("Алекс", 1, 100, 10)
hero2 = Hero("Макс", 2, 80, 15)

# Проверяем первого героя
hero1.greet()
print("Сила до атаки:", hero1.strength)
hero1.attack()
print("Сила после атаки:", hero1.strength)
print("Здоровье до отдыха:", hero1.health)
hero1.rest()
print("Здоровье после отдыха:", hero1.health)

print()

# Проверяем второго героя
hero2.greet()
print("Сила до атаки:", hero2.strength)
hero2.attack()
print("Сила после атаки:", hero2.strength)
print("Здоровье до отдыха:", hero2.health)
hero2.rest()
print("Здоровье после отдыха:", hero2.health)
