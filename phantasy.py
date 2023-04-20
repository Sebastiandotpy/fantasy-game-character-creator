import random

# Define the character classes and their multipliers
classes = {
    'Barbarian': {'Health': 3, 'Strength': 3, 'Magic': 1, 'Initiative': 1},
    'Cleric': {'Health': 1, 'Strength': 1, 'Magic': 3, 'Initiative': 3},
    'Druid': {'Health': 2, 'Strength': 1, 'Magic': 2, 'Initiative': 2}
}

# Function to generate a random integer between 3 and 15


def generate_stat():
    # generate a random number between 3 and 15 inclusive
    value = random.randint(3, 15)

    # 10% chance of printing value in binary
    if random.random() < 0.1:
        print(f"Value in binary: {bin(value)}")
    # 10% chance of printing value in hex
    elif random.random() < 0.2:
        print(f"Value in hex: {hex(value)}")
    # 80% chance of printing value in decimal
    else:
        print(f"Value: {value}")

    return value

# Function to create a character


def create_character(name):
    char_class = random.choice(list(classes.keys()))
    stats = {stat: generate_stat()
             for stat in ['Health', 'Strength', 'Magic', 'Initiative']}
    for stat, multiplier in classes[char_class].items():
        stats[stat] *= multiplier
    return name, char_class, stats


# Ask the user how many characters to create
num_characters = int(input("How many characters do you want to create? "))

# Ask the user for character names, one for each character
character_names = []
for i in range(num_characters):
    name = input("Enter name of character {}: ".format(i+1))
    character_names.append(name)

# Generate the team of characters
team = []
for name in character_names:
    character = create_character(name)
    team.append(character)

# Print out the team
for character in team:
    print("Name: {}".format(character[0]))
    print("Class: {}".format(character[1]))
    print("Health: {}".format(character[2]['Health']))
    print("Strength: {}".format(character[2]['Strength']))
    print("Magic: {}".format(character[2]['Magic']))
    print("Initiative: {}".format(character[2]['Initiative']))
    print()
