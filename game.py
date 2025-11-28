import random


class Player:
    def __init__(self):
        # Old version example: player = {"x":0, "y":0, "coin":0, "hp":10}
        player = {"x": 0, "y": 0, "coin": 0, "hp": 10}

        # Initialize instance attributes from dict keys/values
        for k, v in player.items():
            setattr(self, k, v)

    def move(self, direction, map_size):
        """
        Update x/y based on direction, staying inside the map.
        Returns True if moved, False if invalid/boundary.
        """
        d = direction.lower().strip()
        dx, dy = 0, 0

        if d in ("w", "up", "n", "north"):
            dy = -1
        elif d in ("s", "down", "south"):
            dy = 1
        elif d in ("a", "left", "west"):
            dx = -1
        elif d in ("d", "right", "east"):
            dx = 1
        else:
            return False

        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < map_size and 0 <= ny < map_size:
            self.x, self.y = nx, ny
            return True

        return False


class GameMap:
    def __init__(self):
        self.size = 9

    def draw(self, player):
        """
        Old: draw_ui(x, y)
        New: draw(player) -> use player.x / player.y
        """
        size = self.size
        px, py = player.x, player.y

        print(f"Position: ({px},{py}) | HP: {player.hp} | Coins: {player.coin}")
        print("Controls: W/A/S/D (or up/down/left/right), Q to quit\n")

        for y in range(size):
            row = []
            for x in range(size):
                row.append("P" if (x == px and y == py) else ".")
            print(" ".join(row))
        print()


class Game:
    def __init__(self):
        self.game_name = "Coin Quest"
        self.name = "Player"
        self.events = [
            {"name": "Found a coin", "desc": "You spot a shiny coin on the ground.", "coin": +1, "hp": 0},
            {"name": "Lost a coin", "desc": "A hole in your pocket claims a coin. Rude.", "coin": -1, "hp": 0},
            {"name": "Minor trap", "desc": "A hidden trap snaps at your ankles.", "coin": 0, "hp": -2},
            {"name": "First-aid kit", "desc": "You patch yourself up.", "coin": 0, "hp": +2},
            {"name": "Treasure stash!", "desc": "Jackpot! You find a little stash.", "coin": +3, "hp": 0},
        ]

        self.player = Player()
        self.map = GameMap()

    def check_event(self):
        # Old: player["coin"] ...
        # New: self.player.coin ...
        if random.random() > 0.45:  # 45% chance of an event
            return

        event = random.choice(self.events)

        self.player.coin = max(0, self.player.coin + event["coin"])
        self.player.hp = max(0, min(20, self.player.hp + event["hp"]))

        print(f"Event: {event['name']} — {event['desc']}")
        if event["coin"]:
            sign = "+" if event["coin"] > 0 else ""
            print(f"  Coins {sign}{event['coin']} (now {self.player.coin})")
        if event["hp"]:
            sign = "+" if event["hp"] > 0 else ""
            print(f"  HP {sign}{event['hp']} (now {self.player.hp})")
        print()

    def play(self):
        # Old: main()
        print(f"=== {self.game_name} ===")
        entered = input("What is your name? ").strip()
        if entered:
            self.name = entered
        print(f"Welcome, {self.name}! Collect 10 coins to win.\n")

        while True:
            self.map.draw(self.player)

            if self.player.hp <= 0:
                print("You ran out of HP. Game over!")
                break
            if self.player.coin >= 10:
                print("You collected 10+ coins. You win!")
                break

            cmd = input("Move: ").strip()
            if not cmd:
                continue
            if cmd.lower() in ("q", "quit", "exit"):
                print("Bye!")
                break

            moved = self.player.move(cmd, self.map.size)
            if not moved:
                print("Invalid move (or boundary). Try W/A/S/D.\n")
                continue

            self.check_event()


if __name__ == "__main__":
    Game().play()
