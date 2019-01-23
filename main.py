import pygame
import random


class Body(object):
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = (255, 0, 0)
        self.width = 20
        self.height = 20

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def equal(self, x, y):
        return x == self.x and y == self.y


def generate_food_loc(snake):
    while True:
        food_x = random.randrange(0, 501, 20)
        food_y = random.randrange(0, 501, 20)
        for part in snake:
            if not part.equal(food_x, food_y):
                return food_x, food_y


def main():
    pygame.init()

    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Snake")

    snake = []
    head = Body(240, 240, 0, 0)
    snake.append(head)

    food_x, food_y = generate_food_loc(snake)
    food_width = 20
    food_height = 20

    run = True
    while run:
        pygame.time.delay(100)

        new_head = Body(snake[0].x, snake[0].y, snake[0].x_vel, snake[0].y_vel)
        new_head.x += new_head.x_vel
        new_head.y += new_head.y_vel
        snake.insert(0, new_head)

        if snake[0].equal(food_x, food_y):
            food_x, food_y = generate_food_loc(snake)
            pygame.draw.rect(win, (0, 255, 0), (food_x, food_y, food_width, food_height))
        else:
            snake.pop()

        itr = iter(snake)
        next(itr)
        for part in itr:
            if snake[0].equal(part.x, part.y):
                run = False
                break

        pygame.display.update()

        if snake[0].x < 0 or snake[0].y < 0 or snake[0].x > 500 or snake[0].y > 500:
            run = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            snake[0].x_vel = -20
            snake[0].y_vel = 0
        elif keys[pygame.K_RIGHT]:
            snake[0].x_vel = 20
            snake[0].y_vel = 0
        elif keys[pygame.K_UP]:
            snake[0].x_vel = 0
            snake[0].y_vel = -20
        elif keys[pygame.K_DOWN]:
            snake[0].x_vel = 0
            snake[0].y_vel = 20

        win.fill((0, 0, 0))
        for part in snake:
            part.draw(win)
        pygame.draw.rect(win, (0, 255, 0), (food_x, food_y, food_width, food_height))
        pygame.display.update()

    pygame.quit()


main()
