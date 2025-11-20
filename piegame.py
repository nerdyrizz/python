import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("My first game screen")

image = pygame.image.load("pie.jpg")
image_rect = image.get_rect()  # get image size
screen_rect = screen.get_rect()

# center the image rect on the screen rect
image_rect.center = screen_rect.center

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((58, 58, 58))  # optional: clears screen
    screen.blit(image, image_rect)
    pygame.display.update()

pygame.quit()
