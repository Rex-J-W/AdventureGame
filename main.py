import random


# defines a tile on the map
class Tile:
    def __init__(self, tileID, location, enemies, enemyStrength):
        self.tileID = tileID
        self.location = location
        self.enemies = enemies
        self.enemyStrength = enemyStrength


# runs the game and sets variables
def game():
    running = True
    mapSize = 100
    position = [mapSize // 2, mapSize // 2]
    tiles = [[0] * mapSize] * mapSize
    health = 100
    troops = 700
    strength = 4
    tile = None

    # creates map location templates
    militia = Tile(0, 'militia', 10, 2)
    army = Tile(1, 'army', 100, 5)
    city = Tile(2, 'city', 1000, 7)
    capitol = Tile(3, 'capitol', 2000, 15)
    locations = [militia, army, city, capitol]

    # adds militias to the map
    for i in range(10):
        x = random.randint(0, mapSize - 1)
        y = random.randint(0, mapSize - 1)
        tiles[x][y] = militia.tileID

    # adds armies to the map
    for i in range(5):
        x = random.randint(0, mapSize - 1)
        y = random.randint(0, mapSize - 1)
        tiles[x][y] = army.tileID

    # adds cities to the map
    for i in range(3):
        x = random.randint(0, mapSize - 1)
        y = random.randint(0, mapSize - 1)
        tiles[x][y] = city.tileID

    # adds a capitol to the map
    for i in range(1):
        x = random.randint(0, mapSize - 1)
        y = random.randint(0, mapSize - 1)
        tiles[x][y] = capitol.tileID

    # prints instructions
    print("(commands: north, south, east, west, fight, end)\nWhen using a direction put a number of spaces after it\n"
          "ex: north 5 ; west 7\n\n")

    # game loop
    while running:
        # calls for user input
        action = input("Enter Next Action: ")
        # breaks down user input
        action = action.lower()
        split = action.split()

        # checks commands
        move = [0, 0]
        if split[0] == "north":
            move[1] = int(split[1])
            health += 5
        elif split[0] == "south":
            move[1] = -int(split[1])
            health += 5
        elif split[0] == "east":
            move[0] = int(split[1])
            health += 5
        elif split[0] == "west":
            move[0] = -int(split[1])
            health += 5
        elif split[0] == 'fight':

            # simulates a fight against enemies
            if strength >= tile.enemyStrength and health > 0 and troops > tile.enemies:
                strength += tile.enemyStrength
                health -= 10
                troops += tile.enemies
                tiles[position[0]][position[1]] = 0
                print("Enemies Conquered!")
            else:
                print("You Were Defeated!")
                print("Game Over!")
                running = False
                continue

        # ends the game
        elif split[0] == "end":
            running = False
            continue

        moved = [position[0], position[1]]
        tileID = 0

        # moves the player across the map and checks if it hits any locations on the way
        if move[0] != 0:
            for i in range(abs(move[0])):
                moved[0] = position[0] + (i + 1) * (move[0] // abs(move[0]))
                if moved[0] < 0 or moved[0] >= mapSize:
                    print("Reached the end of the world!")
                    break
                elif tiles[moved[0]][moved[1]] != 0:
                    tileID = tiles[moved[0]][moved[1]]
                    break
        elif move[1] != 0:
            for i in range(abs(move[1])):
                moved[1] = position[1] + (i + 1) * (move[1] // abs(move[1]))
                if moved[1] < 0 or moved[1] >= mapSize:
                    print("Reached the end of the world!")
                    break
                elif tiles[moved[0]][moved[1]] != 0:
                    tileID = tiles[moved[0]][moved[1]]
                    break

        # prints stats
        health = min(health, 100)
        position = [max(min(moved[0], mapSize - 1), 0), max(min(moved[1], mapSize - 1), 0)]
        print("\n\n\t----- Stats -----")
        print("\t\tPosition: " + str(position))
        print("\t\tHealth: " + str(health))
        print("\t\tTroops: " + str(troops))
        print("\t\tStrength: " + str(strength) + "\n\n")

        # checks if the player is at a location
        if tileID != 0:
            tile = locations[tileID - 1]
            print("You have found a(n) " + tile.location + "!  Will you fight or move on?\n\n")
        else:
            tile = None
            print("There is nothing here for you.\n\n")


# runs the game
if __name__ == '__main__':
    game()
