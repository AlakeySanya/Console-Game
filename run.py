import random
import time


class Boss:
    def __init__(self, name, damage, hp, weak, resist):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.weak = weak
        self.resist = resist


class Hero:
    def __init__(self, name, damage, hp, resist, weak=None):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.weak = weak
        self.pick = 0
        self.resist = resist


class Mob:
    def __init__(self, name, damage, hp, weak, resist):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.weak = weak
        self.resist = resist


# Создание боссов
eikthyr = Boss("Eikthyr", [35, "Blunt"], 500, "Pierce", [None])
the_elder = Boss("The Elder", [45, "Slash"], 1000, "Slash", ["Magic", "Pierce"])
bonemass = Boss("Bonemass", [60, "Blunt"], 2000, "Blunt", ["Pierce"])
modir = Boss("Modir", [70, "Frost"], 3000, "Blunt", ["Slash"])
gullveig = Boss("Gullveig", [100, "Fire"], 4500, "Pierce", ["Blunt"])
fenrir = Boss("Fenrir", [120, "Slash"], 10000, "Pierce", ["Blunt", "Frost"])
jotunn = Boss("Jotunn", [200, "Blunt"], 20000, "Blunt", ["Slash", "Pierce"])

# Создание героев
warrior = Hero("Warrior", [30, "Slash"], 600, [None])
archer = Hero("Archer", [40, "Pierce"], 400, [None])
spartan = Hero("Spartan", [35, "Pierce"], 500, ["Slash"])
mage = Hero("Wizard", [45, "Magic"], 350, ["Pierce"])
mauler = Hero("Mauler", [25, "Blunt"], 800, ["Slash", "Pierce", "Blunt"])
god_of_war = Hero("God of War", [10**100, "God"], 10**100, ["Slash", "Pierce", "Magic", "Blunt"])


# Создание мобов
dragon_of_inferno = Mob("Dragon Of Inferno", [40, "Fire"], 650, "Frostbane", ["Slash"])
ice_golem = Mob("Ice golem", [20, "Blunt"], 350, "Fire", ["Slash"])
spider = Mob("Spider", [5, "Pierce"], 50, "Pierce", [None])
skeleton = Mob("Skeleton", [10, "Slash"], 100, "Blunt", ["Slash", "Pierce"])
draugr = Mob("Draugr", [25, "Slash"], 300, None, ["Magic"])
wolf = Mob("Wolf", [35, "Pierce"], 150, "Slash", [None])
troll = Mob("Troll", [40, "Blunt"], 650, "Pierce", ["Blunt"])

# Добавление в список
heroes = [warrior]
pick = 0
for hero in heroes:
    pick += 1
    hero.pick = pick

bosses = [eikthyr, the_elder, bonemass, modir, gullveig, fenrir, jotunn]

# Game stat
round_count = 1


def have_hp():
    for hero in heroes:
        if hero.hp <= 0:
            heroes.remove(hero)
    if not heroes:
        return False
    return True


def round_start(enemy):
    print(f"Heroes left >>> |", end="")
    for hero in heroes:
        print(f"<{hero.name}>|", sep="", end="")
    print()
    damage = 0
    damage_type = ""
    while True:
        curr_hero = input(f"Pick a Hero to attack > ")
        try:
            if int(curr_hero) > len(heroes):
                print(f"Invalid answer, you have only {len(heroes)} heroes")
                continue
        except Exception as ex:
            print(f"Invalid answer, try again.")
            continue
        for hero in heroes:
            if curr_hero == str(hero.pick):
                damage = hero.damage[0]
                damage_type = hero.damage[1]
                curr_hero = hero
        break
    time.sleep(0.5)
    print(f"{curr_hero.name} ready to fight, take a moment and ... ", end="")

    attack_res = attack()

    curr_hero.hp -= attack_res[1]
    if len(attack_res) != 3:
        print(damage * attack_res[0], end="")
        if enemy.weak == damage_type:
            print(f" x 2 (for {enemy.name} weakness)")
        if enemy.resist == damage_type:
            print(f" x 0.5 (for {curr_hero.name} weakness)")
    if enemy.weak == damage_type:
        damage *= 2
    if enemy.resist == damage_type:
        damage *= 0.5
    enemy.hp -= damage * attack_res[0]
    print(f"Total Damage = {damage * attack_res[0]}")

    print()
    print(f"Enemy ({enemy.name}) HP Left = {enemy.hp} ")
    print(f"{curr_hero.name} HP Left = {curr_hero.hp}")
    input("Continue >>> ")
    print()


def attack():
    # Генерируем случайное время задержки
    delay_time = random.uniform(3, 10)

    time.sleep(delay_time)

    start_time = time.time()
    input("Punch!!!")
    print()

    # Считаем, сколько времени прошло от начала до момента ввода
    elapsed_time = time.time() - start_time

    print(f"You punch after {round(elapsed_time, 2)} seconds...")
    if elapsed_time < 0.2:
        print("It was too fast, you miss!!! And lose 30 hp!")
        return [0, 30, 0]
    if elapsed_time < 0.5:
        print("COMBOCRIT and +10 hp!!!\nDamage x 3 = ", end="")
        return [3, -10]
    elif elapsed_time < 0.75:
        print("Crit!!!\nDamage x 2 = ", end="")
        return [2, 0]
    elif elapsed_time < 0.90:
        print("Good!\nDamage x 1 = ", end="")
        return [1, 0]
    elif elapsed_time < 1.0:
        print("Norm. You lose 5 hp.\nDamage x 0.8 = ", end="")
        return [0.8, 10]
    elif elapsed_time < 1.3:
        print("Lil bit late, but still ok. You lose 10 hp.\nDamage x0.5 = ", end="")
        return [0.5, 20]
    else:
        print("Its was too late, you miss!!! And lose 30 hp!")
        return [0, 30, 0]


def enemy_atack(enemy):
    print(f"{enemy.name} turn to Attack")
    print("Wait... ", end="")
    time.sleep(3)
    print("BAM!!!!")
    time.sleep(0.5)
    for hero in heroes:
        damage = random.randrange(enemy.damage[0] - int(enemy.damage[0] * 0.2),
                                  enemy.damage[0] + int(enemy.damage[0] * 0.2))
        hero.hp -= damage
        print(hero.name, "took damage... ", f"-{damage}", f"hp. {hero.hp} hp Left")
        time.sleep(1)
    input("Continue >>> ")
    print()


def check_person_stats():
    print()
    while True:
        ch = input("Wanna check persons stats? [y/n] >>> ")
        if ch == "y":
            for hero in heroes:
                print(f"{hero.name}'s hp - {hero.hp} weak({hero.weak}),"
                      f" damage - {hero.damage[0]} type({hero.damage[1]}),"
                      f" resists - {hero.resist}")
                input("Continue >>> ")
                print()
            break
        elif ch == "n":
            break
        else:
            print("Invalid answer, try again.")


def battle_with(enemy):
    print()
    check_person_stats()
    while True:
        if not have_hp():
            print("All you heroes are dead...")
            break
        round_start(enemy)
        if enemy.hp <= 0:
            print(f"{enemy.name} defeated...")
            break
        enemy_atack(enemy)


print("\nWelcome to the mystical realm of Eldoria!")
time.sleep(1)
print(f"You've got a new Person - {warrior.name}!")
time.sleep(1)

print()
print("You find yourself in the small village of Oakhaven, surrounded by ancient forests and towering mountains.")
input("Press Enter to continue...")

print("Rumors have been spreading about the awakening of powerful bosses threatening the land.")
input("Press Enter to continue...")

print("As a brave hero, you embark on a journey to defeat these mighty foes and restore peace to Eldoria.")
input("Press Enter to continue...")

print("Your adventure begins! Your first challenge awaits in the dark woods to the east.")
input("Press Enter to enter the woods...")

print("As you venture deeper, you encounter a vile creature - a giant spider!")
input("Press Enter to prepare for battle...")

battle_with(spider)

print("Victorious, you emerge from the woods, but more challenges lie ahead.")
input("Press Enter to continue your journey...")

print("You decide to rest and recover in Oakhaven before facing the next challenge.")
input("Press Enter to rest...")

print(f"You find a helmet while you was resting!")
input("Press Enter to equip the Helemet")

warrior.resist = ["Blunt"]
warrior.hp += 100

print(f"You are now equipped with {warrior.name}'s new armor, Helmet! (+Blunt resist and 100 hp)")
input("Press Enter to continue your journey...")

print("While in Oakhaven, you hear rumors of a legendary sword hidden in the Caverns of Eternal Frost.")
input("Press Enter to set off for the Caverns...")

print("The journey to the caverns is treacherous, filled with icy winds and dangerous creatures.")
input("Press Enter to face the challenges...")

print("Upon reaching the entrance, you encounter a guardian ice golem blocking the way.")
input("Press Enter to prepare for battle...")

battle_with(ice_golem)

print("After a fierce battle, the guardian is defeated, and you enter the Caverns of Eternal Frost.")
input("Press Enter to explore the caverns...")

print("Deep within, you find the legendary sword, Frostbane, known for its ability to freeze enemies.")
input("Press Enter to claim Frostbane...")

warrior.damage = [40, "Frostbane"]

print(f"You are now equipped with {warrior.name}'s new weapon, Frostbane!")
input("Press Enter to continue your journey...")

print("As you leave the caverns, you receive a message from the mystical Oracle of Eldoria.")
input("Press Enter to listen to the Oracle's message...")

print("The Oracle reveals that a powerful boss, the Dragon of Inferno, has awakened in the Volcanic Peaks.")
input("Press Enter to set off for the Volcanic Peaks...")

print("The path to the peaks is perilous, filled with lava rivers and volcanic eruptions.")
input("Press Enter to navigate the dangerous terrain...")

print("At the summit, you face the mighty Dragon of Inferno, spewing flames and wreaking havoc.")
input("Press Enter to prepare for the ultimate battle...")

battle_with(dragon_of_inferno)

print("With great effort, you defeat the Dragon of Inferno, bringing peace back to Eldoria.")
print("You are hailed as a hero, and your journey is celebrated across the land.")
input("Press Enter to bask in your victory...")

print("Congratulations! You have successfully completed your quest in the mystical realm of Eldoria.")


