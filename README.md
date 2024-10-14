# Text-Based RPG Adventure Game

This project is a command-line interface (CLI) text-based RPG game where you explore a world, fight enemies, and visit shops to buy food, armor, and weapons to help you in combat. The game features random events like combat encounters and opportunities to equip the player with better items.

## Features

- **Player Movement**: Move around a 2D grid map and encounter different stores or enemies.
- **Combat System**: Fight random enemies with health and damage mechanics.
- **Shops**: Purchase food, armor, and weapons from various stores to enhance your character's abilities.
- **Inventory**: Keep track of purchased items, such as food for healing or armor for defense.
- **Random Enemies**: Fight a variety of enemies like the Weak Elephant or Biggest Chungus with varying health levels.

## Classes

### Enemy
Represents enemies you encounter during combat.

- `get_enemy_name()`: Returns the name of the enemy.
- `get_enemy_health()`: Returns the health of the enemy.
- `health_consume(damage)`: Reduces the enemy's health by the given damage.

### Food
Represents healing items you can purchase from the store.

- `get_food_name()`: Returns the name of the food.
- `get_healing()`: Returns the healing amount of the food.

### Armour
Represents defensive equipment that reduces incoming damage from enemies.

- `get_armour_name()`: Returns the name of the armor.
- `get_armour_defense()`: Returns the defense multiplier for the armor.

### Weapon
Represents weapons used to deal damage in combat.

- `get_weapon_name()`: Returns the name of the weapon.
- `get_damage()`: Returns the damage dealt by the weapon.

## Game Flow

### Overworld
- The player moves around the overworld map using north, south, east, and west commands.
- When landing on special locations, the player can enter stores to purchase items or encounter enemies for combat.

### Combat
- Players can attack enemies, use items from their inventory, or run away.
- Critical hits have a 10% chance to occur, dealing 400% damage.

## Inventory System
- Players can collect food, armor, and weapons in their inventory.
- Food can be used to heal during combat.
- Armor reduces damage taken from enemy attacks.

## Installation

To run the game, simply download the file and run it with Python.

```bash
python game.py
