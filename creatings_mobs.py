from functions import *


class Boss:
    def __init__(self, name, damage, dmg_type, hp, weak, resist):
        self.name = name
        self.damage = damage
        self.dmg_type = dmg_type
        self.hp = hp
        self.weak = weak
        self.resist = resist


class Hero:
    def __init__(self, name, damage, dmg_type, hp, resist, weak):
        self.name = name
        self.damage = damage
        self.dmg_type = dmg_type
        self.hp = hp
        self.weak = weak
        self.pick = 0
        self.resist = resist


class Mob:
    def __init__(self, name, damage, dmg_type, hp, weak, resist):
        self.name = name
        self.damage = damage
        self.dmg_type = dmg_type
        self.hp = hp
        self.weak = weak
        self.resist = resist


# Создание боссов
eikthyr = Boss("Eikthyr", 50, "Blunt", 1000, "Pierce", ["Slash"])
'''the_elder = Boss("The Elder", [45, "Slash"], 1000, "Slash", ["Magic", "Pierce"])
bonemass = Boss("Bonemass", [60, "Blunt"], 2000, "Blunt", ["Pierce"])
modir = Boss("Modir", [70, "Frost"], 3000, "Blunt", ["Slash"])
gullveig = Boss("Gullveig", [100, "Fire"], 4500, "Pierce", ["Blunt"])
fenrir = Boss("Fenrir", [120, "Slash"], 10000, "Pierce", ["Blunt", "Frost"])
jotunn = Boss("Jotunn", [200, "Blunt"], 20000, "Blunt", ["Slash", "Pierce"])'''

# Создание героев
warrior = Hero("Warrior", 10, ["Slash"], 200, [], [""])
archer = Hero("Archer", 20, ["Pierce"], 150, [], [""])
'''spartan = Hero("Spartan", [35, "Pierce"], 500, ["Slash"])
mage = Hero("Wizard", [45, "Magic"], 350, ["Pierce"])
mauler = Hero("Mauler", [25, "Blunt"], 800, ["Slash", "Pierce", "Blunt"])
god_of_war = Hero("God of War", [10**100, "God"], 10**100, ["Slash", "Pierce", "Magic", "Blunt"])'''


# Создание мобов
spider = Mob("Spider", 5, ["Pierce"], 50, "Pierce", [])
ice_golem = Mob("Ice golem", 20, ["Blunt"], 350, "Fire", ["Slash"])
dragon_of_inferno = Mob("Dragon Of Inferno", 40, ["Fire"], 650, "Frostbane", ["Slash"])
'''skeleton = Mob("Skeleton", [10, "Slash"], 100, "Blunt", ["Slash", "Pierce"])
draugr = Mob("Draugr", [25, "Slash"], 300, None, ["Magic"])
wolf = Mob("Wolf", [35, "Pierce"], 150, "Slash", [None])
troll = Mob("Troll", [40, "Blunt"], 650, "Pierce", ["Blunt"])'''

# Выбор по числам
heroes = [warrior]
pick = 0
for hero in heroes:
    pick += 1
    hero.pick = pick

# Рюкзачек героев
heroes_items = ["Heal Poison", "Damage Poison", "Strength Poison"]

