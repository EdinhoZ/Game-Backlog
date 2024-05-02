import pygame

pygame.init()

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
background_colour = (255, 255, 255)
pygame.display.set_caption('Game Backlog')
screen.fill(background_colour)

pygame.display.flip()

class Button():
    def __init__(self, text, x, y, width, height, colour):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, 1, (0, 0, 0))
        screen.blit(text, (self.x + self.width / 2 - text.get_width() / 2, self.y + self.height / 2 - text.get_height() / 2))


add_game_button = Button('Add Game', 50, 50, 700, 300, (255, 255, 255))
exit_button = Button('Exit', 50, 350, 700, 300, (255, 255, 255))



running = True
while running:
    add_game_button.draw(screen)
    exit_button.draw(screen)
    if add_game_button.clicked:
        # add mechanic to add a game from an API of games
        print('Select game to add')
    if exit_button.clicked:
        running = False
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False