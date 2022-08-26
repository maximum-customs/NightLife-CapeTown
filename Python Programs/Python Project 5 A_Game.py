import pygame
from math import degrees, pi, radians, sin, cos, atan, sinh, sqrt
import random
from pygame.mouse import get_cursor

from pygame.sprite import RenderClear
pygame.init()
display_info = pygame.display.Info()
WIDTH, HEIGHT = 1500, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
run = True
clock = pygame.time.Clock()


class Object:
    def __init__(self, solid, colour, coordinate):
        self.solid = solid
        self.colour = colour
        self.coordinate = coordinate

class Rectangle(Object):
    def __init__(self, solid, colour, coordinate, height, width):
        super().__init__(solid, colour, coordinate)
        self.height = height
        self.width = width
        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1], self.width, self.height)


class Tile(Rectangle):
    def __init__(self, solid, colour, coordinate, height = 25, width = 25):
        super().__init__(solid, colour, coordinate, height, width)
class Grass(Tile):
    def __init__(self, solid, coordinate, colour = (0, 200, 0), height = 25, width = 25):
        super().__init__(solid, colour, coordinate, height, width)
class Water(Tile):
    def __init__(self, solid, coordinate, colour = (0, 0, 200), height = 25, width = 25):
        super().__init__(solid, colour, coordinate, height, width)


Level_Map = [[[35,[0, 59]],[34, [0, 59], [28, 59]],[33,[0, 59]],[32,[0, 59]]],[[33, [25, 27]],[32, [0, 59]]]]

Map_Tile_List = []

def Map_draw(Level_Map):
    for tile_type in Level_Map:
        for row in tile_type:
            y_tile_value = row[0]
            for x_section in row[1:]:
                x_tile_value = x_section[0]
                while x_tile_value <= x_section[1]:
                    x_coordinate_value = x_tile_value* 25
                    y_coordinate_value = y_tile_value* 25
                    if tile_type == Level_Map[0]:
                        Map_Tile_List.append(Grass(True, (x_coordinate_value, y_coordinate_value)))
                    if tile_type == Level_Map[1]:
                        Map_Tile_List.append(Water(True, (x_coordinate_value, y_coordinate_value)))
                    x_tile_value += 1









Map_draw(Level_Map)

while run:                                      #Running the 
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    mouse_press = pygame.mouse.get_pressed()
    if mouse_press[0] == True:
        mouse_pos = pygame.mouse.get_pos()
        rounded_mouse_pos0 = (round((mouse_pos[0]- 12.5)/25))*25
        rounded_mouse_pos1 = (round((mouse_pos[1]- 12.5)/25))*25
        Map_Tile_List.append(Grass(True, (rounded_mouse_pos0, rounded_mouse_pos1)))
    screen.fill((10, 100, 160))
    for tile in Map_Tile_List:
        pygame.draw.rect(screen, tile.colour, tile.rect)
    pygame.display.update()
