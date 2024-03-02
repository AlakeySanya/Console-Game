class Enemy:
    def __init__(self, name, damage, dmg_type, hp, weak, resist):
        """Инициализация объекта Босс."""
        self.name = name
        self.damage = damage
        self.dmg_type = dmg_type
        self.hp = hp
        self.weak = weak
        self.resist = resist


class Hero:
    def __init__(self, name, damage, dmg_type, hp, resist, weak):
        """Инициализация объекта Герой."""
        self.name = name
        self.damage = damage
        self.dmg_type = dmg_type
        self.hp = hp
        self.weak = weak
        self.resist = resist
        self.id = 0  # Переменная для отслеживания порядка в списке


# Создание боссов
eikthyr = Enemy("Eikthyr", 50, "Blunt", 1000, "Pierce", ["Slash"])

# Новые идеи боссов
'''the_elder = Boss("The Elder", [45, "Slash"], 1000, "Slash", ["Magic", "Pierce"])
bonemass = Boss("Bonemass", [60, "Blunt"], 2000, "Blunt", ["Pierce"])
modir = Boss("Modir", [70, "Frost"], 3000, "Blunt", ["Slash"])
gullveig = Boss("Gullveig", [100, "Fire"], 4500, "Pierce", ["Blunt"])
fenrir = Boss("Fenrir", [120, "Slash"], 10000, "Pierce", ["Blunt", "Frost"])
jotunn = Boss("Jotunn", [200, "Blunt"], 20000, "Blunt", ["Slash", "Pierce"])'''


# Создание героев
warrior = Hero("Warrior", 10, ["Slash"], 200, [], [""])
archer = Hero("Archer", 20, ["Pierce"], 150, [], [""])

# Новые идеи героев
'''spartan = Hero("Spartan", [35, "Pierce"], 500, ["Slash"])
mage = Hero("Wizard", [45, "Magic"], 350, ["Pierce"])
mauler = Hero("Mauler", [25, "Blunt"], 800, ["Slash", "Pierce", "Blunt"])
god_of_war = Hero("God of War", [10**100, "God"], 10**100, ["Slash", "Pierce", "Magic", "Blunt"])'''


# Создание мобов
spider = Enemy("Spider", 5, ["Pierce"], 50, "Pierce", [])
ice_golem = Enemy("Ice Golem", 15, ["Blunt"], 350, "Fire", ["Slash"])
dragon_of_inferno = Enemy("Dragon Of Inferno", 30, ["Fire"], 750, "Frost", ["Slash"])

# Список героев
heroes = [warrior]

# Список Предметов
hero_items = []
