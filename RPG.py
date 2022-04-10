import os
import random

#CHRISTIE  
class Enemy:
  def __init__ (self, name: str, health: int) -> None:
    self.name = name
    self.health = health
    
  def get_enemy_name (self):
    return self.name

  def get_enemy_health (self):
    return self.health
  
  # Taking Health method
  def health_consume (self, damage: int) -> int:
    self.health -= damage
    return self.health

# Enemy Class End

# SOGOL
class Food:
    def __init__(self, option: str, name: str, healing: int) -> None:
        self.name = name
        self.healing = healing
        self.option = option

    def __str__(self):
      return f"[{self.option}] {self.name}: Provides {self.healing} HP"
  
    def get_food_name (self):
        return self.name
        
    def get_healing (self):
        return self.healing

    def option (self):
        return self.option 
    
#HALLE
class Armour:
    def __init__(self, option: str, name: str, defense: int)-> None:
        self.option = option
        self.name = name
        self.defense = defense
    
    def __str__(self):
      return f"[{self.option}] {self.name}: Reduces attacks by {self.defense}"
  
    def get_armour_name(self):
        return self.name

    def get_armour_defense(self):
        return self.defense

    def option(self):
        return self.option
    
    def use_armour(self, damage: int) -> int:
        damage *= self.defense 
        return self.defense

#IRWIN
class Weapon:
    def __init__(self, option: str, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage
        self.option = option

    def __str__(self):
      return f"[{self.option}] {self.name}: Deals {self.damage} damage."
  
    def get_weapon_name (self):
        return self.name
        
    def get_damage (self):
        return self.damage

    def option (self):
        return self.option 

enemies = [
  Enemy("Weak Elephant", 50),
  Enemy("Fat Horse", 100),
  Enemy("Big Leopard", 100),
  Enemy("Biggest Chungus", 300),
]

health_list = [
  Food("1","Snozzcumbers", 30),
  Food("2", "Frobscottle", 50),
  Food("3", "Quogwinkle", 100),
]

armour_list = [
  Armour("1", "Titanium Shield", 0.5),
  Armour("2", "Hamster Bubble", 0.9),
  Armour("3", "Karuta", 0.2),
]

weapon_list = [
  Weapon("1", "Stick", 15),
  Weapon("2", "Dagger", 25),
  Weapon("3", "Sword", 35),
]

base_map = [
    [".", ".", ".", ".", "."],
    [".", ".", "$", ".", "."],
    [".", ".", ".", ".", "."],
    [".", "E", ".", ".", "."],
    [".", ".", ".", ".", "W"],
    ["A", ".", ".", ".", "."]
]


level = [
    [".", ".", ".", ".", "."],
    [".", ".", "$", ".", "."],
    [".", ".", ".", ".", "."],
    [".", "E", ".", ".", "."],
    [".", ".", ".", ".", "W"],
    ["A", ".", ".", ".", "."],
]
# Create empty list for inventory
inventory = ["== INVENTORY ==", ]


player_health = 100
player_crit_chance = 10
player_strength = 20
player_defense = 0
armour_defense = 0


#enemy_name = "Zombie Wizard"
#enemy_health = 100

# pick random enemy from list
enemy = random.choice(enemies)

# Player starts at location (0, 0)
x = 0
y = 0

location = "overworld"


# CLI - Command-line interface

while True:
    if location == "overworld":
        level[y][x] = "P"

        # draw map
        for row in level:
            for c in row:
                print(c, end=" ")
            print()

        print()
        
        # player details
        print(f"You are at location ({x}, {y}).")

        # store at (3, 0)
        if base_map[y][x] == "$":
            print("You arrive at the store.")
            print("[1] Enter the store")
            
        elif base_map[y][x] == "E":
            location = "Combat"
            continue

        elif base_map[y][x] == "A":
            print("[2] Enter the Armour Store")

        elif base_map[y][x] == "W":
            print("[3] Enter the Weapons Store")
            
        print()

        # menu options
        print("Choose direction to move:")
        print("[N]orth")
        print("[S]outh")
        print("[E]ast")
        print("[W]est")

        # get choice
        choice = input("choice: ").upper()

        level[y][x] = base_map[y][x]

        # handle choice
        if choice == "N":
            y -= 1
        elif choice == "S":
            y += 1
        elif choice == "E":
            x += 1
        elif choice == "W":
            x -= 1
        elif choice == "1":
            location = "Food Store"
        elif choice == "2":
            location = "Armour Store"
        elif choice == "3":
            location = "Weapons"
            
    elif location == "Food Store":
      # description / menu
        print("You are now in the store")
            
        while True: # Shop Loop
                
            # Print Foods in list
            for f in health_list:
                print(f)
            
            print("[4] Exit")
            
            # user choice
            choice_number = input("Choice: ")
            for f in health_list:
                if choice_number == f.option:
                
            # handle the choice
                    food_name = f.get_food_name()
                    food_health = f.get_healing()
                    print(f"\nYou chose {food_name}. Use when you are dying.")
                    print()
                
                # append to inventory list
                    inventory.append("\n")
                    inventory.append(f"{food_name}, Provides {food_health} HP.")
                
            if choice_number == "4":
                location = "overworld"
                level[y][x] = base_map[y][x]
                y -= 1
                break
                
        os.system("clear")

    elif location == "Armour Store":
        print("You are now in the Armour store")
        
        while True: 
                
            # Print Foods in list
            for a in armour_list:
                print(a)
            
            print("[4] Exit")
            print()
            
            # user choice
            choice_number = input("Choice: ")
            for a in armour_list:
                if choice_number == a.option:
                
            # handle the choice
                    armour_name = a.get_armour_name()
                    armour_defense = a.get_armour_defense()
                    print(f"\nYou chose {armour_name}. Use when you need.")
                    print()
                    inventory.append("\n")
                    inventory.append(f"{armour_name}, Reduces enemy attacks by {armour_defense} of original HP.")
                
            if choice_number == "4":
                location = "overworld"
                level[y][x] = base_map[y][x]
                y -= 1
                break

    elif location == "Weapons":
      # description / menu
        print("Wow! So many weapons!")
            
        while True: # Weapons Loop
                
            # Print Foods in list
            for w in weapon_list:
                print(w)
            
            print("[4] Exit")
            print()
            
            # user choice
            choice_number = input("Choice: ")
            for w in weapon_list:
                if choice_number == w.option:
                
            # handle the choice
                    weapon_name = w.get_weapon_name()
                    weapon_damage = w.get_damage()
                    print(f"\nYou picked up {weapon_name}. Deals {weapon_damage} damage.")
                    print()
                
                # append to inventory list
                    inventory.append("\n")
                    inventory.append(f"{weapon_name}, Provides {weapon_damage} HP.")
                
            if choice_number == "4":
                location = "overworld"
                level[y][x] = base_map[y][x]
                y -= 1
                break
                
        os.system("clear")
    
    elif location == "Combat":
        os.system("clear")
        print("You are ambushed!")
        print()

        # Choose a random enemy
        enemy = random.choice(enemies)
        # Get Name and Stats of chosen Enemy
        enemy_name = enemy.get_enemy_name()
        enemy_health = enemy.get_enemy_health()

        while True:  # combat loop
            # description / menus
            
            # Print Player Stats
            print(f"Player: {player_health} HP")
            
            # Print Enemy Stats
            print(f"{enemy_name}: {enemy_health} HP")

            # Print Player Defense
            print(f"Defense: {player_defense} HP")
            print()
            print("[1] Attack")
            print("[2] Use All Item")
            print("[3] Run away")
          
            # get user choice
            print()
            choice = input("Choice: ")
            print() 
            
            # handle the choice
            if choice == "1":  # attack
                damage = random.randrange(20, 50)
                damage = damage + player_strength * 0.5
                print(damage)
                print(f"You hit {enemy_name} for {damage}")
                enemy_health = enemy.health_consume(damage)    
              
            elif choice == "2":  # items
                print(*inventory)
                print()
                player_health += food_health
                pass
            
            elif choice == "3":  # run
                location = "overworld"
                level[y][x] = base_map[y][x]
                y -= 1
                break
            
            if enemy_health <= 0:  # enemy defeated
                location = "overworld"
                base_map[y][x] = "."
                print(f"You defeated {enemy_name}.")
                print()
                input("Press ENTER to continue")
                break

            # enemy move
            damage = random.randrange(10, 20)
            print(f"{enemy_name} hits you for {damage} hp.")

            if armour_defense > 0:
              damage = (damage * armour_defense)
              print(f"With your {armour_name}, the damage was reduced to {damage}")
            player_health -= damage
            
            # crit chance 10%
            roll = random.randrange(100)
            if roll >= 90:
                print("CRITICAL HIT")
                damage *= 4  # crit damage = 400%

            player_health -= damage
            
            

            input("Press ENTER to continue")

            if player_health <= 0:  # player defeat
                pass  # ?? what do you do at this point?
            
            os.system("clear")

    
    os.system("clear")
