import pygame
from math import degrees, pi, radians, sin, cos, atan, sinh, sqrt
import random

from pygame import draw




pygame.init()
display_info = pygame.display.Info()
WIDTH, HEIGHT = 1500, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
run = True
clock = pygame.time.Clock()




class Circle:
    def __init__(self, colour, centre, radius, vx, vy, density):
        self.radius = radius
        self.centre = centre
        self.vx = vx
        self.vy = vy
        self.colour = colour
        self.density = density
        self.mass = density* pi* radius**2
        self.momentum_x = density* pi* (radius**2) *self.vx
        self.momentum_y = density* pi* (radius**2) *self.vy
    def draw_circle(self):
        pygame.draw.circle(screen, self.colour , self.centre, self.radius, 0, True, True, True, True)

    def displacement(self):
        self.centre[0] += self.vx
        self.centre[1] += self.vy
    





#C1 = Circle([100,100,200], [300,200], 100, 2, 0, 3)
#C2 = Circle([100,10,10], [600,500], 100, 0, -2, 4)
circle_list = []                                                                         #List of all circles
#circle_list.append()
for i in range(20):
    circle_list.append(Circle([100,80,80], [random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)], 40, random.randint(-10,10), random.randint(-10,10), 10))





def Collision_scan( circlea, circleb):                                                        #checking if circles collide
    #course_x = ((circlea.vx + circlea.centre[0]) - (circleb.vx + circleb.centre[0]))
    #course_y = ((circlea.vy + circlea.centre[1]) - (circleb.vy + circleb.centre[1]))
    #if course_x >= 0 and course_y >= 0 :                                                     #using velocitiy and direction to determine if circles can collide
        
        Sum_Radius = (circlea.radius + circleb.radius)
        Distance = sqrt((circlea.centre[0] - circleb.centre[0])**2 + (circlea.centre[1] - circleb.centre[1])**2)
        if Sum_Radius >= Distance:
            Forcex = circlea.mass * circlea.vx - circleb.mass * circleb.vx
            if circlea.centre[0] <= circleb.centre[0]:
                circlea.vx -= Forcex/circlea.mass
                circleb.vx += Forcex/circleb.mass
            else:
                circlea.vx += Forcex/circlea.mass
                circleb.vx -= Forcex/circleb.mass
            Forcey = circlea.mass * circlea.vy - circleb.mass * circleb.vy
            if circlea.centre[1] <= circleb.centre[1]:
                circlea.vy -= Forcey/circlea.mass
                circleb.vy += Forcey/circleb.mass
            else:
                circlea.vy += Forcey/circlea.mass
                circleb.vy -= Forcey/circleb.mass
                print ( f"{circlea} {circleb} ")
        
        

while run:                                                                      #Running the screen
    clock.tick(FPS)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((40, 50, 100))
                                                                           #running collision scan through circles
    
    for index , circleA  in enumerate(circle_list):
        
        for circleB in circle_list[index:]:
            if circleA is not circleB:
                Collision_scan( circleA, circleB)
            
        


    for circle in circle_list:                                                  #general object functions
        circle.displacement()
        circle.draw_circle()
    pygame.display.update()


