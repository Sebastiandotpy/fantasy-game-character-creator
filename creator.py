import random
# List of possible character types
types = ["Warrior", "Wizard","Potato"]

# Ask user for 5 character namese
names = []
for i in range(5):
    name = input(f"Character {i+1}:")
    names.append(name)

print("Your Characters are complete")

# Generate stats for each character and print them
for name in names:
    # Randomly choose a character type
    character_type = random.choice(types)
    # Generate random stats
    health = random.randint(5, 10) * (3 if character_type == "Potato" else 1)
    strength = random.randint(5, 10) * (3 if character_type == "Warrior" else 1)
    magic = random.randint(5, 10) * (3 if character_type == "Wizzard" else 1)

# Print character information
    print(f'"{name}" is a {character_type}! Strength: {strength}, magic: {magic}, Health: {health}')

    # Print final message
    print("Happy Hunting")