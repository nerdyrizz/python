import pygame
import random

pygame.init()

# CUSTOM EVENT IDS FOR COLOUR CHANGE EVENTS
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# define basic colours using pygame.color
# background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# Sprite class representing a moving object
class Sprite(pygame.sprite.Sprite):

    # constructor method
    def __init__(self,color,height,width):
        # call to the parent class (Sprite) constructor
        super().__init__()
        # create the sprites surface with dimension and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        # set initial velocity with random direction
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    # method to update the sprite's position
    def update(self):
        # move the sprite by its velocity
        self.rect.move_ip(self.velocity)
        # flag to track it sprite hits boundary
        boundary_hit = False
        # check for collision with left or right boundary and reverse directions
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        # check for collision with top or bottom boundary and reverse directions
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

    # if boundary was hit, post a color change event
    if boundary_hit:
        pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
        pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    
    # METHOD TO CHANGE THE SPRITE'S COLOR
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

    #METHOD TO CHANGE THE BACKGROUND COLOR
    def change_background_color():
        global bg_color 
        bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

    # CREATE A GRP TO HOLD SPRITES
    all_sprites_list = pygame.sprite.Group()
    # intantiate a sprite
    sp1 = Sprite(WHITE, 20, 30)
    #radomly position the sprite
    sp1.rect.x = random.randomint(0,480)
    sp1.rect.y = random.randomint(0,370)
    # add the sprite to the grp
    all_sprites_list.add(sp1)

    # create the game window
    screen = pygame.display.set_mode((500, 400))
    # set the window title
    pygame.display.set_caption("Bouncing Sprite with Color Change")
    # set initial background color
    bg_color = BLUE
    # apply the initial background color
    screen.fill(bg_color)

    # game loop control flag
    exit = False
    # create a clock object to manage frame rate
    clock = pygame.time.Clock()

    # main game loop
    while not exit:
        # event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            # if the sprite color change event is detected
            elif event.type == SPRITE_COLOR_CHANGE_EVENT:
                sp1.change_color()
            # if the background color change event is detected
            elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
                change_background_color()
            
    # update all sprites
    all_sprites_list.update()
    # fill the screen with the current background color
    screen.fill(bg_color)
