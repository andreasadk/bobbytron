from pygame.locals import *
import pygame
import sys


pygame.init()


class Player:

    FONT = pygame.font.Font('emulogic.ttf', 20)
    is_dead = False

    def __init__(self, surface, starting_position, name, name_position, name_rotation, color, direction, key_left,
                 key_right):
        self.surface = surface
        self.starting_position = starting_position
        self.name = name
        self.name_position = name_position
        self.name_rotation = name_rotation
        self.color = color
        self.direction = direction
        self.points = [starting_position, starting_position]
        self.head_position = (starting_position[0], starting_position[1])
        self.key_left = key_left
        self.key_right = key_right
        
    def tick(self):
        if not self.is_dead:
            self.move()
            self.check_collisions()
        self.draw()

    def draw(self):
        if len(self.points) > 1:
            pygame.draw.lines(self.surface, self.color, False, self.points, 6)
        pygame.draw.line(self.surface, self.color, self.points[-1], self.head_position, 6)
        if debug:
            hitboxes = self.calc_hitbox()
            for hitbox in hitboxes:
                pygame.draw.rect(SCREEN_SURFACE, (0, 255, 0), hitbox, 1)
            
    def calc_hitbox(self):
        hitbox = []
        print('Body point list: ' + str(self.points))
        print('Head position: ' + str(self.head_position))
        for idx, point in enumerate(self.points):
            hitbox_rect = None
            if idx == 0:
                continue
            if point[1] == self.head_position[1]:
                hitbox_rect = pygame.Rect(pygame.Rect(point[0]-3, point[0]+3, self.head_position[0] - point[1]+9, 6))
                hitbox.append(hitbox_rect)
            #if idx+1 < len(self.points):
            #    next_point = self.points[idx+1]
            #else:
            #    next_point = self.head_position
            #
            ##Horizontal line
            #if point[0] != next_point[0]:
            #    hitbox_rect = pygame.Rect(point[0], point[1], 6, next_point[0])
            ##Vertical line
            #else:
            #    hitbox_rect = pygame.Rect(point[0], point[1], next_point[1], 6)
            hitbox.append(hitbox_rect)
        return hitbox
    
    def check_collisions(self):
        for rect in calc_border_rects():
            if rect.collidepoint(self.head_position[0], self.head_position[1]):
                self.is_dead = True

    def move(self):
        if self.direction == DIRECTION_UP:
            self.head_position = (self.head_position[0], (self.head_position[1] - 1/6))
        elif self.direction == DIRECTION_DOWN:
            self.head_position = (self.head_position[0], (self.head_position[1] + 1/6))
        elif self.direction == DIRECTION_LEFT:
            self.head_position = ((self.head_position[0] - 1/6), self.head_position[1])
        elif self.direction == DIRECTION_RIGHT:
            self.head_position = ((self.head_position[0] + 1/6), self.head_position[1])
            
    def change_direction(self, direction):
        print("Direction before: " + str(self.direction))
        self.direction = direction
        self.points.append(self.head_position);
        print("Direction after: " + str(direction))

    def key_pressed(self, key):
        print("Key pressed: " + str(key))
        if key == self.key_right:
            if self.direction == DIRECTION_UP:
                self.change_direction(DIRECTION_RIGHT)
            elif self.direction == DIRECTION_LEFT:
                self.change_direction(DIRECTION_UP)
            elif self.direction == DIRECTION_RIGHT:
                self.change_direction(DIRECTION_DOWN)
            elif self.direction == DIRECTION_DOWN:
                self.change_direction(DIRECTION_LEFT)
        elif key == self.key_left:
            if self.direction == DIRECTION_UP:
                self.change_direction(DIRECTION_LEFT)
            elif self.direction == DIRECTION_LEFT:
                self.change_direction(DIRECTION_DOWN)
            elif self.direction == DIRECTION_RIGHT:
                self.change_direction(DIRECTION_UP)
            elif self.direction == DIRECTION_DOWN:
                self.change_direction(DIRECTION_RIGHT)


def draw_hud():
    #Draw board
    pygame.draw.rect(SCREEN_SURFACE, (0, 255, 255), border, 10)
    for rect in calc_border_rects():
        pygame.draw.rect(SCREEN_SURFACE, (255, 255, 255), rect, 1)
    
    #center_header = BACKGROUND_FONT.render("*BOBBYTRON*", 1, (229,204,142))
    #center_header_rotated = pygame.transform.rotate(center_header, 180)
    #SCREEN_SURFACE.blit(center_header_rotated, (300,300))
    for player in players:
        player_name = player.FONT.render(player.name, 1, player.color)
        SCREEN_SURFACE.blit(pygame.transform.rotate(player_name, player.name_rotation), player.name_position)

def calc_border_rects():
    return [pygame.Rect(50-4, 50-4, 1170+10, 10), pygame.Rect(50-4, 50-4, 10, 620), pygame.Rect(50-4, 669-4, 1170+10, 10), pygame.Rect(1220-4, 50-4, 10, 620)] 

#pygame setup
pygame.display.set_caption('BobbyTron')
SCREEN_SURFACE = pygame.display.set_mode((1280, 720))
debug = False
#game vars
DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'
DIRECTION_LEFT = 'left'
DIRECTION_RIGHT = 'right'
player1 = Player(SCREEN_SURFACE, (90,95), 'Pink', (100, 15), 180, (255, 0 , 255), DIRECTION_RIGHT, K_LEFT, K_RIGHT)
player2 = Player(SCREEN_SURFACE, (90,105), 'Green', (15, 100), 270, (0, 255, 0), DIRECTION_DOWN, K_n, K_m)
player3 = Player(SCREEN_SURFACE, (565,105), 'Red', (15, 575), 270, (255, 0, 0), DIRECTION_UP, K_x, K_c)
player4 = Player(SCREEN_SURFACE, (90,105), 'Blue', (15, 100), 270, (0, 255, 0), DIRECTION_DOWN, K_n, K_m)
player5 = Player(SCREEN_SURFACE, (90,105), 'Yellow', (15, 100), 270, (0, 255, 0), DIRECTION_DOWN, K_n, K_m)
player6 = Player(SCREEN_SURFACE, (90,105), 'Orange', (15, 100), 270, (0, 255, 0), DIRECTION_DOWN, K_n, K_m)
player7 = Player(SCREEN_SURFACE, (90,105), 'White', (15, 100), 270, (0, 255, 0), DIRECTION_DOWN, K_n, K_m)
player8 = Player(SCREEN_SURFACE, (90,105), 'Purple', (15, 100), 270, (0, 255, 0), DIRECTION_DOWN, K_n, K_m)
players = [player1]
border = pygame.Rect(50, 50, 1170, 620)


#main game loop
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
           
        if event.type == KEYDOWN:
            for player in players:
                player.key_pressed(event.key)

    draw_hud()
    for player in players:
        player.tick()
    
    pygame.display.update()