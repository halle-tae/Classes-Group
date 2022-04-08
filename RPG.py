import os
import random
  
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

# Enemy Class Ends

class Food:
    def __init__(self, option: int, name: str, healing: int) -> None:
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

    def add_healing (self, healing: int) -> int:
        self.healing += healing
        return self.healing
    

enemies = [
  Enemy("Weak Elephant", 50),
  Enemy("Fat Horse", 100),
  Enemy("Big Leopard", 100),
  Enemy("Biggest Chungus", 300),
]

health_food = [
  Food("1","Snozzcumbers", 30),
  Food("2", "Frobscottle", 50),
  Food("3", "Quogwinkle", 100),
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
            location = "combat"
            continue
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
            location = "store"

    elif location == "store":
      
      # description / menu
      print("You are now in the store")

      while True: # Shop Loop
      
        # Print Foods in list
        for f in health_food:
          print(f)
        
        print("[E] Exit")
      
      
        
        # user choice
        choice_number = input("Choice: ")
        for f in health_food:
          if choice_number == f.option:
            
        # handle the choice
            
            food_name = f.get_food_name()
            food_health = f.get_healing()
         

            print(f"\nYou chose {food_name}. Please use me               when you are dying.")
            
            # append to inventory list
            
            inventory.append("\n")
            inventory.append(f"{food_name}, Provides {food_health} HP.")
            
    elif choice == "E":
        location = "overworld"
        level[y][x] = base_map[y][x]
        y -= 1
        break
        
    elif location == "combat":
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

            print("[1] Attack")
            print("[2] Item")
            print("[3] Run away")
          
            # get user choice
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
                input("Press ENTER to continue")
                break

            # enemy move
            damage = random.randrange(10, 20)
            
            # crit chance 10%
            roll = random.randrange(100)
            if roll >= 90:
                print("CRITICAL HIT")
                damage *= 4  # crit damage = 400%

            player_health -= damage
            
            print(f"{enemy_name} hits you for {damage} hp.")

            input("Press ENTER to continue")

            if player_health <= 0:  # player defeat
                pass  # ?? what do you do at this point?
            
            os.system("clear")



    
    os.system("clear")
