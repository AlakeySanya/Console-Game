import random
import time

from creating_objects import *


def have_hp():
    """Проверяет наличие hp у героев."""
    for hero in heroes:
        if hero.hp <= 0:
            heroes.remove(hero)
    return bool(heroes)


def round_start(enemy):
    """Описывает начало нового раунда битвы."""
    print("Heroes left >>> |", end="")
    for hero in heroes:
        print(f"<{hero.name}>|", sep="", end="")
    print()
    order_in_hero_list()
    curr_hero = ""

    while True:
        curr_hero_number = input("Pick a Hero to attack > ")
        # Чит код на hp
        if curr_hero_number == "666":
            hp = input("How much? > ")
            for hero in heroes:
                hero.hp += int(hp)
            continue
            # Чит код на damage
        if curr_hero_number == "777":
            damage = input("How much? > ")
            for hero in heroes:
                hero.damage += int(damage)
            continue
        try:
            if int(curr_hero_number) > len(heroes):
                print(f"Invalid answer, you have only {len(heroes)} heroes")
                continue
            else:
                break
        except ValueError:
            print("Invalid answer, try again.")
            continue

    for hero in heroes:
        if str(hero.id) == curr_hero_number:
            curr_hero = hero
            break

    time.sleep(0.5)
    print(f"{curr_hero.name} ready to fight, take a moment and ... ", end="")
    attack_res = attack()
    apply_attack_results(curr_hero, enemy, curr_hero.damage, curr_hero.dmg_type, attack_res)
    total_damage = curr_hero.damage * attack_res[0]
    if enemy.weak in curr_hero.dmg_type:
        total_damage *= 2
    if enemy.resist in curr_hero.dmg_type:
        total_damage *= 0.5
    print(f"Total Damage = {total_damage}")
    print()
    print(f"Enemy ({enemy.name}) HP Left = {enemy.hp} ")
    print(f"{curr_hero.name} HP Left = {curr_hero.hp}")
    input("Continue >>> ")
    print()


def attack():
    """Определяет результат атаки."""
    delay_time = random.uniform(3, 10)
    time.sleep(delay_time)
    start_time = time.time()
    input("Punch!!!\n\n")
    elapsed_time = time.time() - start_time
    print(f"You punch after {round(elapsed_time, 2)} seconds...")

    if elapsed_time < 0.2:
        print("It was too fast, you miss!!! And lose 30 hp!")
        return [0, 30]
    elif elapsed_time < 0.48:
        print("COMBOCRIT and +10 hp!!!\nDamage x 3 = ", end="")
        return [3, -10]
    elif elapsed_time < 0.55:
        print("Crit!!!\nDamage x 2 = ", end="")
        return [2, 0]
    elif elapsed_time < 0.70:
        print("Good!\nDamage x 1 = ", end="")
        return [1, 0]
    elif elapsed_time < 0.80:
        print("Norm. You lose 5 hp.\nDamage x 0.8 = ", end="")
        return [0.8, 10]
    elif elapsed_time < 1.0:
        print("Lil bit late, but still ok. You lose 10 hp.\nDamage x0.5 = ", end="")
        return [0.5, 20]
    else:
        print("Its was too late, you miss!!! And lose 30 hp!")
        return [0, 30]


def apply_attack_results(curr_hero, enemy, damage, damage_type, attack_res):
    """Применяет результаты атаки к героям и врагу."""
    curr_hero.hp -= attack_res[1]

    if not attack_res[0]:
        print(damage * attack_res[0])

    if enemy.weak in damage_type:
        print(f" x 2 (for {enemy.name} weakness)")
    if enemy.resist in damage_type:
        print(f" x 0.5 (for {curr_hero.name} weakness)")

    if enemy.weak in damage_type:
        damage *= 2
    if enemy.resist in damage_type:
        damage *= 0.5

    enemy.hp -= damage * attack_res[0]


def enemy_attack(enemy):
    """Описывает ход врага в битве."""
    print(f"{enemy.name} turn to Attack")
    print("Wait... ", end="")
    time.sleep(3)
    print("BAM!!!!")
    time.sleep(0.5)

    for hero in heroes:
        damage = random.randrange(
            enemy.damage - int(enemy.damage * 0.2),
            enemy.damage + int(enemy.damage * 0.2)
        )
        hero.hp -= damage
        print(f"{hero.name} took damage... ", f"-{damage}", f"hp. {hero.hp} hp Left")
        time.sleep(1)

    input("Continue >>> ")
    print()


def check_person_stats():
    """Выводит статистику персонажей."""
    while True:
        ch = input("Wanna check persons stats? [y/n] >>> ")
        if ch == "y":
            for hero in heroes:
                heroe_weakness = [hero.weak for hero in heroes]
                hero_dmg_type = [hero.dmg_type for hero in heroes]
                hero_resists = [hero.resist for hero in heroes]
                print(
                    f"{hero.name}'s hp {hero.hp} | damage {hero.damage} type{hero_dmg_type} | "
                    f"weaknesses - {heroe_weakness} | resists - {hero_resists}"
                )
                input("Continue >>> ")
                print()
            break
        elif ch == "n":
            print()
            break
        else:
            print("Invalid answer, try again.")


def battle_with(enemy):
    """Запускает битву с врагом."""
    print()
    check_person_stats()

    while True:
        if not have_hp():
            print("You lose. All heroes hp gone...")
            raise Exception("You Lose")
        round_start(enemy)
        wanna_use_item(enemy)

        if enemy.hp <= 0:
            print(f"{enemy.name} defeated...")
            break

        enemy_attack(enemy)


def use_item(item, hero, enemy):
    """Применяет предмет к герою или врагу."""
    if item == "Heal Poison":
        hero.hp += 200
    elif item == "Damage Poison":
        enemy.hp -= 300
    elif item == "Strength Poison":
        hero.damage += 20
    elif item == "Apple":
        hero.hp += 30
        hero.damage += 2


def wanna_use_item(enemy):
    """Проверяет, хочет ли игрок использовать предмет."""
    if not hero_items:
        return None

    while True:
        ch = input("Wanna use an item? [y/n] >>> ")
        if ch == "y":
            print("Items:", end="")
            for item in hero_items:
                print(f"<{item}>|", end="")
            print()

            while True:
                item = input("Which item do you wanna choose? >>> ")
                if item not in hero_items:
                    print("No such item found.")
                else:
                    for hero in heroes:
                        print(f"<{hero.name}>|", sep="", end="")
                    print()

                    while True:
                        choose_hero = input("On which hero? >>> ")
                        try:
                            if int(choose_hero) > len(heroes):
                                print(f"Invalid answer, you have only {len(heroes)} heroes")
                                continue
                        except ValueError:
                            print("Invalid answer, try again.")
                            continue

                        for hero in heroes:
                            if choose_hero == str(hero.id):
                                choose_hero = hero
                                break

                        use_item(item, choose_hero, enemy)
                        hero_items.remove(item)
                        return

        elif ch == "n":
            return
        else:
            print("Invalid answer, try again.")


def print_storyline(storyline):
    if len(storyline) < 90:
        print(storyline)
        input("Press Enter to continue...")
        return None
    chars_to_new_line = " .,"
    curr_line = ""
    # Для вывода сюжета в консоли
    count = 0
    for char in storyline:
        count += 1
        curr_line += char
        if count >= 70 and char in chars_to_new_line:
            count = 0
            print(curr_line)
            curr_line = ""
    print(curr_line)
    input("Press Enter to continue...")
    print()


def order_in_hero_list():
    """Присваивает каждому герою свой 'id' для удобного выбора героя."""
    next_id = 1
    for hero in heroes:
        hero.id = next_id
        next_id += 1
