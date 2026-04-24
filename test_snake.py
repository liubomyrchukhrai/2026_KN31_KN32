import unittest
from snake import SnakeLogic

class TestSnake(unittest.TestCase):
    def setUp(self):
        # Ініціалізація гри перед кожним тестом
        self.game = SnakeLogic(600, 400, 20)

    def test_initial_state(self):
        # Перевірка початкових значень
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.direction, "RIGHT")
        self.assertFalse(self.game.game_over)

    def test_move_increases_head(self):
        # Перевірка, що після руху вправо координата X голови збільшилась
        old_head = self.game.snake[0]
        self.game.move()
        new_head = self.game.snake[0]
        self.assertEqual(new_head[0], old_head[0] + 20)

    def test_change_direction_valid(self):
        # Перевірка зміни напрямку
        self.game.change_direction("UP")
        self.assertEqual(self.game.direction, "UP")

    def test_change_direction_invalid(self):
        # Перевірка заборони розвороту на 180 градусів
        self.game.change_direction("LEFT") # Початковий RIGHT, LEFT не має спрацювати
        self.assertEqual(self.game.direction, "RIGHT")

    def test_collision_with_wall(self):
        # Виводимо змійку за межі екрана
        self.game.snake = [(0, 0)]
        self.game.direction = "LEFT"
        self.game.move()
        self.assertTrue(self.game.game_over)

    def test_eat_food(self):
        # Ставимо їжу прямо перед змійкою
        self.game.snake = [(100, 100)]
        self.game.direction = "RIGHT"
        self.game.food = (120, 100)
        self.game.move()
        
        # Змійка мала з'їсти їжу: довжина 2 (виросла), рахунок 1
        self.assertEqual(len(self.game.snake), 2)
        self.assertEqual(self.game.score, 1)

if __name__ == '__main__':
    unittest.main()