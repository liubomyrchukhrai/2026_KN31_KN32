import pygame
import random

class SnakeLogic:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.score = 0
        self.food = self._generate_food()
        self.game_over = False

    def _generate_food(self):
        x = random.randrange(0, self.width, self.cell_size)
        y = random.randrange(0, self.height, self.cell_size)
        return (x, y)

    def move(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == "UP": head_y -= self.cell_size
        elif self.direction == "DOWN": head_y += self.cell_size
        elif self.direction == "LEFT": head_x -= self.cell_size
        elif self.direction == "RIGHT": head_x += self.cell_size

        new_head = (head_x, head_y)

        # Перевірка на зіткнення зі стінами або собою
        if (head_x < 0 or head_x >= self.width or 
            head_y < 0 or head_y >= self.height or 
            new_head in self.snake):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Перевірка на їжу
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
        else:
            self.snake.pop()

    def change_direction(self, new_dir):
        # Заборона розвороту на 180 градусів
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir

# --- Візуалізація (запускається, якщо файл основний) ---
if __name__ == "__main__":
    pygame.init()
    cell = 20
    w, h = 600, 400
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    game = SnakeLogic(w, h, cell)

    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: game.change_direction("UP")
                if event.key == pygame.K_DOWN: game.change_direction("DOWN")
                if event.key == pygame.K_LEFT: game.change_direction("LEFT")
                if event.key == pygame.K_RIGHT: game.change_direction("RIGHT")

        game.move()
        
        screen.fill((0, 0, 0))
        for segment in game.snake:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, cell, cell))
        pygame.draw.rect(screen, (255, 0, 0), (*game.food, cell, cell))
        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()