import pygame
import random 
pygame.init()

# constants for easier adjustment
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# LOAD N TRANSFORM THE BG IMAGE 
background_image = pygame.transform.scale(pygame.image.load("bg.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# load font once at beggining
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("dogderblue")) # bg color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0,0,width,height), 5)
        self.rect = self.image.get_rect()

    def move(self,x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

# setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite collision")
all_sprites = pygame.sprite.Group()

# create sprites
sprite1 = Sprite(pygame.Color("black"), 20,30)
sprite1.rect.x , sprite1.rect.y = random.randint(0, (SCREEN_WIDTH - sprite1.rect.width)), random.randint(0, (SCREEN_HEIGHT - sprite1.rect.height))
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color("red"), 20,30)
sprite2.rect.x , sprite2.rect.y = random.randint(0, (SCREEN_WIDTH - sprite2.rect.width)), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

# game loop control variables
running = True
won = False
clock = pygame.time.Clock()

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
        
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
