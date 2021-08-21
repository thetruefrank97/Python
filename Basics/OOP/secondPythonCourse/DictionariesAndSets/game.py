locations = {
    0: "You are sitting in front of a computer learning python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "YOu are in a valley besdie a stream",
    5: "You are in the forest"
}

exits = [
   {"Q": 0},
    {"W": 2, "2": 2,  "E": 3, "3": 3,  "N": 5, "5": 5,  "S": 4, "4": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5"
    }

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exists are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
