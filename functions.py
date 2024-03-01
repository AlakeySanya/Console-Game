import random
import time
from creatings_mobs import *


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
                damage = hero.damage
                damage_type = hero.dmg_type
                curr_hero = hero
        break
    time.sleep(0.5)
    print(f"{curr_hero.name} ready to fight, take a moment and ... ", end="")

    attack_res = attack()

    curr_hero.hp -= attack_res[1]
    if len(attack_res) != 3:
        print(damage * attack_res[0])
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
        damage = random.randrange(enemy.damage - int(enemy.damage * 0.2),
                                  enemy.damage + int(enemy.damage * 0.2))
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
                heroe_weakness = [hero.weak for hero in heroes]
                hero_dmg_type = [hero.dmg_type for hero in heroes]
                hero_resists = [hero.resist for hero in heroes]
                print(f"{hero.name}'s hp {hero.hp}"
                      f" | damage {hero.damage} type{hero_dmg_type}"
                      f" | weaknesses - {heroe_weakness}"
                      f" | resists - {hero_resists}")
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
        wanna_use_item(enemy)
        if enemy.hp <= 0:
            print(f"{enemy.name} defeated...")
            break
        enemy_atack(enemy)


def use_item(item, hero, enemy):
    if item == "Heal Poison":
        hero.hp += 200
    elif item == "Damage Poison":
        enemy.hp -= 300
    elif item == "Strength Poison":
        hero.damage += 20


def wanna_use_item(enemy):
    if not heroes_items:
        return None
    while True:
        ch = input("Wanna use an item? [y/n] >>> ")
        if ch == "y":
            print("Items:", end="")
            for item in heroes_items:
                print(f"<{item}>|", end="")
            print()
            while True:
                item = input("Which item do you wanna choose? >>> ")
                if item not in heroes_items:
                    print("No such item found.")
                else:
                    for hero in heroes:
                        print(f"<{hero.name}>|", sep="", end="")
                    print()
                    while True:
                        ch_hero = input("On which hero? >>> ")
                        try:
                            if int(ch_hero) > len(heroes):
                                print(f"Invalid answer, you have only {len(heroes)} heroes")
                                continue
                        except Exception as ex:
                            print(f"Invalid answer, try again.")
                            continue
                        for hero in heroes:
                            if ch_hero == str(hero.pick):
                                ch_hero = hero
                        break
                    use_item(item, ch_hero, enemy)
                    heroes_items.remove(item)
                    return None
        elif ch == "n":
            return None
        else:
            print("Invalid answer, try again.")

