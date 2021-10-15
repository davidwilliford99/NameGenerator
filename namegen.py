import pygame 
import random


# For this program, click generate to generate a random name from the names list
# To clear the name, click the black space anywhere under the generate button
# YOU MUST CLEAR NAME AFTER EVERY USE 


# pygame startup
pygame.init()
window = pygame.display.set_mode((720,500)) 
title = pygame.display.set_caption("Random Name Selector")


# font setup
pygame.font.init()
myfont = pygame.font.SysFont('Typewriter', 72)
buttonFont = pygame.font.SysFont('Typewriter', 30)


# list of names
names = ["David Williford", "Someone Else", "Elon Musk", "Jethro Libutan", "Bill Gates", "Jeff Bezos", "Joe Rogan"] 


# creates generate button
button = pygame.Rect(320, 300, 100, 25)  # creates a rect object
bg = bg = [0, 0, 0]
window.fill(bg)
pygame.draw.rect(window, [255, 255, 255], button)  # draw button


# function for finding and displaying random name
def random_nameGen():
    # clears last name
    button = pygame.Rect(320, 300, 100, 25)  # creates a rect object
    bg = bg = [0, 0, 0]
    window.fill(bg)
    pygame.draw.rect(window, [255, 255, 255], button)
    window.blit(buttonText, btnTextRect)


    # displays random name 
    random_name = random.choice(names)
    displayText = myfont.render(random_name, True, (255, 255, 255))
    textRect = displayText.get_rect()
    textRect.center = (360, 200)
    window.blit(displayText, textRect)
    return random_name


# Generate button text
buttonText = buttonFont.render("Generate", True, (0, 0, 0))
btnTextRect = buttonText.get_rect()
btnTextRect.center = (370, 313)
window.blit(buttonText, btnTextRect)


# run section 
run = True 

while run:
    pygame.display.update()
    pygame.time.delay(100)


    # if red X is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # when mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos  # gets mouse position

        # checks if mouse position is over the button
        if button.collidepoint(mouse_pos):
            random_nameGen()


pygame.quit

