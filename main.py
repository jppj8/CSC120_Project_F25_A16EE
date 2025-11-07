# main.py
import random

# ====== YOUR ORIGINAL CODE (kept as-is) ======
game_name = "Chef!"  # TODO, name your game project Python
print("Welcome", game_name)
print("=============")
print("Are you ready to cook!")  # TODO, print greetings with game name
name = input("Before we start cooking what is your name?")
print(f"Let's cook some food Chef " + name + "!")

# 2.2 Dictionary for player stats
player = {
    "name": name,
    "wealth": 100,
    "cooking skills": 0
}

# 2.3 Random events
events = ["learn a new skills", "meet a contender", "do nothing chill relax"]
event = random.choice(events)
print(f"While cooking, you {event}!")

# 2.4 Update character stats
if event == "learn a new skills":
    player["cooking skills"] += 1
    print(f"{player['name']} learned a new skill, you now have {player['cooking skills']} skills!.")
elif event == "meet a contender":
    player["wealth"] -= 10
    print(f"{player['name']} got beaten during cook off with another chef, wealth is now {player['wealth']}.")
# if event is "do nothing chill relax", nothing happens


# ====== PROJECT 3 ADDITIONS (built on your code) ======

# 4) Add player position
player["x"] = 0
player["y"] = 0

# 5) Global map size (9x9, 0..8 with goal at bottom-right)
map_size = 9

# 2 & 3) Move event logic into a function with NO prints
def check_event():
    """
    Randomly apply one of the events to the player.
    No printing here (per Part 3 spec). Returns the chosen event string.
    """
    chosen = random.choice(events)
    if chosen == "learn a new skills":
        player["cooking skills"] += 1
    elif chosen == "meet a contender":
        player["wealth"] -= 10
    # "do nothing chill relax" => no stat change
    return chosen

# 6) Draw the UI: grid + HUD (C = player, M = goal)
def draw_ui(x: int, y: int):
    print("=" * 25)
    for row in range(map_size):
        for col in range(map_size):
            if row == y and col == x:
                ch = "C"
            elif row == map_size - 1 and col == map_size - 1:
                ch = "M"
            else:
                ch = "."
            print(ch, end="  ")
        print()
    print("=" * 25)
    print(f"Wealth: {player['wealth']}")
    print("-" * 25)
    print(f"Cooking Skills: {player['cooking skills']}")
    print("=" * 25)

# 7) Movement with bounds (w/a/s/d)
def move(direction: str):
    if direction == "w" and player["y"] > 0:
        player["y"] -= 1
    elif direction == "a" and player["x"] > 0:
        player["x"] -= 1
    elif direction == "s" and player["y"] < map_size - 1:
        player["y"] += 1
    elif direction == "d" and player["x"] < map_size - 1:
        player["x"] += 1
    else:
        print("You cannot move that way!")

# 8) Main game loop
def main():
    # First UI and prompt
    draw_ui(player["x"], player["y"])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != "q":
        # Move player
        move(direction)

        # Check for reaching the goal (gate)
        if player["x"] == map_size - 1 and player["y"] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        # Apply a silent event (no prints)
        _ = check_event()

        # Redraw and prompt again
        draw_ui(player["x"], player["y"])
        direction = input("Your next move (w/a/s/d/q): ")

# 9) Run
if __name__ == "__main__":
    main()
