import random


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


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")
        self.strength -= 1


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")
        self.strength -= 1


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")
        self.strength -= 1


warrior = Warrior("Warrior", 1, 100, 10, 20)
mage = Mage("Mage", 1, 80, 15, 30)
assassin = Assassin("Assassin", 1, 90, 12, 25)

choice = input("Выберите героя: Warrior / Mage / Assassin: ").strip().lower()

if choice == "warrior":
    player = warrior
elif choice == "mage":
    player = mage
elif choice == "assassin":
    player = assassin
else:
    player = None
    print("Такого героя нет. Запустите программу и введите Warrior, Mage или Assassin.")

if player is not None:
    opponent = random.choice([warrior, mage, assassin])

    print("Вы выбрали:", player.name)
    print("Противник:", opponent.name)

    # Один метод attack() работает по-разному у разных классов.
    player.attack()
    opponent.attack()

    # Warrior — камень, Assassin — ножницы, Mage — бумага.
    if player == opponent:
        print("Ничья!")
    elif player == warrior and opponent == assassin:
        print(player.name, "победил!")
    elif player == assassin and opponent == mage:
        print(player.name, "победил!")
    elif player == mage and opponent == warrior:
        print(player.name, "победил!")
    else:
        print(opponent.name, "победил!")
