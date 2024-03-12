from functions import *
from creating_objects import *


print("Created by Alexander Burmitskiy in 2024")
time.sleep(2)
input("Welcome to Eldoria...")
print()

print_storyline("In the mystical realm of Eldoria, a dark force has cast its"
                " shadow over the once peaceful lands. Creatures of darkness"
                " roam freely, threatening the existence of the Eldorian people."
                " As a seasoned warrior, you embark on a quest to rid Eldoria of "
                "this malevolent presence and restore balance.")
                
print_storyline("You start your journey in the quaint village of Elmsworth."
                " The villagers share tales of strange occurrences, missing"
                " townsfolk, and a growing darkness in the nearby forests.")

print_storyline("You are a warrior, equipped with a sword and filled with"
                " enthusiasm for adventure. Consequently, you head towards the forest.")
print_storyline("Here you find big spider! Fight him!!!")

battle_with(spider)

print_storyline("After defeating the spider, you continue onward in search of more adventures"
                " and to rescue the inhabitants of Eldoria. Along the way, you find an apple and decide to keep it."
                "(+ 30 hp + 2 damage after eating)")

hero_items.append("Apple")

print_storyline("You come across the mountains, feeling cold and in need of shelter."
                " Finding a cave, you decide to enter it when suddenly.")

print_storyline("A ICE GOLEM EMERGES FROM IT!!!")

battle_with(ice_golem)

print_storyline("After defeating the ice golem, you entered the cave from which it emerged."
                " In the depth of the cave, you noticed something reflecting the sunlight...")

print_storyline("It was the mighty Frostbane, a great icy power. You decided to take this sword with you."
                "(+ 10 damage + damage type Frost)")

warrior.damage += 10
warrior.dmg_type.append("Frost")

print_storyline("The defeat of the Ice Golem reveals a deeper conspiracy. A dragon known as Inferno Dragon"
                " has been awakened, spreading chaos across the lands of Eldoria. The village of Emberfall"
                " is under siege, and its people turn to you for salvation.")

print_storyline("Stepping onto the fiery lands, the chill of your sword seems to be your salvation. But suddenly...")

print_storyline("A DRAGON COMES FOR YOU!!!")

battle_with(dragon_of_inferno)

print_storyline("After that fight you find a man that looks like he wont to go with you."
                " He have a bow and looks pretty strong. (+new hero archer)")

print_storyline("You rest a lot before go to the next enemy (+ 100 hp to anyone)")

heroes.append(archer)

for hero in heroes:
    hero.hp += 100

print_storyline("After all that crap that happen you deside to go to the last monster --The Elder--"
                "and finish him")

print_storyline("LETS GOOOOOOOOOOOOOOO")

battle_with(the_elder)

print("You win!!! Game over.")