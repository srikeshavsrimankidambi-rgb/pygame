import pygame
#Note this code will not run as it is incomplete.
WIDTH = 800
HEIGHT = 600

# This is the class for the Player:
class Player:
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.x = 0
        self.y = 0
        self.speed = 5

#This is the function to draw the player's health bar on the screen:
# Sorry, I'm doing this because I don't know how to code it if the health bar is a picture.
def draw_player_health(screen, player):
    pygame.draw.rect(screen, (255,0,0),
                     (20,20,200,20))

    pygame.draw.rect(screen, (0,255,0),
                     (20,20,
                      200 * player.health/player.max_health,
                      20))

    pygame.draw.rect(screen, (255,255,255),
                     (20,20,200,20), 2)

# This next part of the code is for the enemy class.
# It also makes everything move around the player, so it will look like its view.
class Charger:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 1
        self.speed = 3

    def update(self, player):
        # Move directly at player
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed

        if self.y < player.y:
            self.y += self.speed
        elif self.y > player.y:
            self.y -= self.speed

    def draw(self, screen, player):
        screen_x = self.x - player.x + WIDTH // 2
        screen_y = self.y - player.y + HEIGHT // 2

        pygame.draw.circle(
            screen,
            (255,0,0),
            (int(screen_x), int(screen_y)),
            20
        )

class Poisoner:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 2
        self.speed = 2

    def update(self, player):
        pass

    def die(self):
        # Create poison puddle
        pass

    def draw(self, screen, player):
        screen_x = self.x - player.x + WIDTH // 2
        screen_y = self.y - player.y + HEIGHT // 2

        pygame.draw.circle(
            screen,
            (0,255,0),
            (int(screen_x), int(screen_y)),
            20
        )

class Shooter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 3
        self.speed = 1
        self.shoot_timer = 0

    def update(self, player):
        pass

    def shoot(self):
        pass

    def draw(self, screen, player):
        screen_x = self.x - player.x + WIDTH // 2
        screen_y = self.y - player.y + HEIGHT // 2

        pygame.draw.circle(
            screen,
            (0,0,255),
            (int(screen_x), int(screen_y)),
            20
        )

class Booster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 4
        self.speed = 1

    def update(self, enemies):
        # Buff nearby enemies
        pass

    def draw(self, screen, player):
        screen_x = self.x - player.x + WIDTH // 2
        screen_y = self.y - player.y + HEIGHT // 2

        pygame.draw.circle(
            screen,
            (255,255,0),
            (int(screen_x), int(screen_y)),
            20
        )

# This is the bullet class, which will be used for the shooter's bullets.
class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = 10
        self.damage = 10

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self, screen, player):
        screen_x = self.x - player.x + WIDTH // 2
        screen_y = self.y - player.y + HEIGHT // 2

        pygame.draw.circle(
            screen,
            (255,255,255),
            (int(screen_x), int(screen_y)),
            5
        )

# This draws the crosshair in the middle of the screen.
def draw_crosshair(screen):
    pygame.draw.line(screen,
                     (255,255,255),
                     (WIDTH//2 - 10, HEIGHT//2),
                     (WIDTH//2 + 10, HEIGHT//2))

    pygame.draw.line(screen,
                     (255,255,255),
                     (WIDTH//2, HEIGHT//2 - 10),
                     (WIDTH//2, HEIGHT//2 + 10))
