import unittest
from unittest.mock import patch
from io import StringIO
import random
from game import *


class TestGame(unittest.TestCase):

    # ---------------- Player Tests ----------------
    def test_player_initialization(self):
        p = Player("Alice")
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)
        self.assertEqual(p.health, 100)
        self.assertEqual(p.coin, 0)

    def test_player_movement(self):
        p = Player()
        map_size = 5
        p.move("s", map_size)
        self.assertEqual(p.x, 1)
        p.move("d", map_size)
        self.assertEqual(p.y, 1)
        p.move("w", map_size)
        self.assertEqual(p.x, 0)
        p.move("a", map_size)
        self.assertEqual(p.y, 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_player_invalid_move(self, mock_stdout):
        p = Player()
        p.move("w", 5)
        self.assertIn("You cannot move that way!", mock_stdout.getvalue())

    # ---------------- GameMap Tests ----------------
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_map_draw(self, mock_stdout):
        p = Player()
        gm = GameMap(3)
        gm.draw(p)
        output = mock_stdout.getvalue()
        self.assertIn("C", output)
        self.assertIn("M", output)
        self.assertIn("Health:", output)
        self.assertIn("Coin:", output)

    # ---------------- Game Event Tests ----------------
    def test_check_event_coin(self):
        game = Game()
        game.events = ["find a coin"]
        game.check_event()
        self.assertEqual(game.player.coin, 1)

    def test_check_event_monster(self):
        game = Game()
        game.events = ["meet a monster"]
        game.check_event()
        self.assertEqual(game.player.health, 90)

    def test_check_event_do_nothing(self):
        game = Game()
        game.events = ["do nothing"]
        prev_health = game.player.health
        prev_coin = game.player.coin
        game.check_event()
        self.assertEqual(game.player.health, prev_health)
        self.assertEqual(game.player.coin, prev_coin)

    # ---------------- Game Victory Test ----------------
    @patch('builtins.input', side_effect=["s"]*8 + ["d"]*8)
    @patch('sys.stdout', new_callable=StringIO)
    def test_reach_exit(self, mock_stdout, mock_input):
        game = Game()
        x, y = 0, 0
        while not (game.player.x == game.map_size - 1 and game.player.y == game.map_size - 1):
            game.player.move("s", game.map_size) if game.player.x < game.map_size - 1 else None
            game.player.move("d", game.map_size) if game.player.y < game.map_size - 1 else None
        self.assertEqual(game.player.x, game.map_size - 1)
        self.assertEqual(game.player.y, game.map_size - 1)

if __name__ == "__main__":
    unittest.main()
