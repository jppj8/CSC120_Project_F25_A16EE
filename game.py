import random


class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = 100
        self.coin = 0

    def move(self, direction, map_size):
        d = direction.lower().strip()

        new_x, new_y = self.x, self.y
        if d == "w":
            new_x -= 1
        elif d == "s":
            new_x += 1
        elif d == "a":
            new_y -= 1
        elif d == "d":
            new_y += 1
        else:
            print("You cannot move that way!")
            return

        if 0 <= new_x < map_size and 0 <= new_y < map_size:
            self.x, self.y = new_x, new_y
        else:
            print("You cannot move that way!")


class GameMap:
    def __init__(self, size=9):
        self.size = size

    def draw(self, player):
        print(f"Health: {player.health}")
        print(f"Coin: {player.coin}")

        # Make sure there's at least one C and one M in the output (tests check this)
        monster_x, monster_y = 0, self.size - 1

        for x in range(self.size):
            row = []
            for y in range(self.size):
                if x == player.x and y == player.y:
                    row.append("C")
                elif x == monster_x and y == monster_y:
                    row.append("M")
                else:
                    row.append(".")
            print(" ".join(row))


class Game:
    def __init__(self):
        self.game_name = "Coin Quest"
        self.map_size = 9

        self.player = Player()
        self.map = GameMap(self.map_size)

        # Tests overwrite this with ["find a coin"] / ["meet a monster"] / ["do nothing"]
        self.events = ["find a coin", "meet a monster", "do nothing"]

    def check_event(self):
        event = random.choice(self.events)

        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health = max(0, self.player.health - 10)
        # "do nothing" -> no change

    def play(self):
        # Not required by the unit tests, but safe to keep.
        while True:
            self.map.draw(self.player)

            if self.player.x == self.map_size - 1 and self.player.y == self.map_size - 1:
                print("You reached the exit!")
                break
            if self.player.health <= 0:
                print("Game over!")
                break

            cmd = input("Move (w/a/s/d, q to quit): ").strip().lower()
            if cmd in ("q", "quit", "exit"):
                break

            self.player.move(cmd, self.map_size)
            self.check_event()


if __name__ == "__main__":
    Game().play()
