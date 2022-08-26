import pygame
from math import degrees, pi, radians, sin, cos, atan, sinh, sqrt
import random
pygame.init()
display_info = pygame.display.Info()
WIDTH, HEIGHT = 1500, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
run = True
clock = pygame.time.Clock()


class Sircle:
    def __init__(self, colour, centre, radius, velocity, direction, density):
        self.radius = radius
        self.centre = centre
        self.velocity = velocity
        self.colour = colour
        self.direction = -direction
        self.density = density
        self.mass = density* pi* radius**2
        self.momentum = density* pi* (radius**2) *velocity
        self.last_collision = None
        self.kinetic_energy = ((density* pi* radius**2) / 2) * velocity** 2
        self.velocity_final = velocity
        
    def circle_displacement(self):
        self.centre[0] += self.velocity_final * cos(radians(self.direction))
        self.centre[1] += self.velocity_final * sin(radians(self.direction))
    def draw_circle(self):
        pygame.draw.circle(screen, self.colour , self.centre, self.radius, 0, True, True, True, True)
    def circle_collision(self, circleB):
        Xa, Xb = self.centre[0] , circleB.centre[0]
        Ya, Yb = self.centre[1] , circleB.centre[1]
        Sv = self.velocity
        Bv = circleB.velocity
        Sm = self.mass
        Bm = circleB.mass
        
        self.velocity_final = ((Sm -Bm)/(Sm + Bm))* Sv + ((2*Bm)/(Sm+ Bm))* Bv

        Sd = self.direction
        Bd = 0

        if Xa < Xb:
            Bd = degrees(atan((Yb - Ya) / (Xb - Xa))) + 180
        elif Xa > Xb:
            Bd = degrees(atan((Yb - Ya) / (Xb - Xa)))
        else:
            if Ya > Yb:
                Bd = 90
            elif Ya < Yb:
                Bd = -90
        Sdf = ( 2*Bd - Sd -180)
        ChaA = Bd - Sd
        while ChaA > 180:
            ChaA -= 360
        while ChaA < -180:
            ChaA += 360
        #ChaA_final = ChaA* (1/(1 + self.momentum))
        #Sdf = Sd + ChaA_final
        #ChaA = Sdf - Sd
        #Sdf = Sd + (ChaA)/2
        #ChaAF = ChaA* (circleB.mass / self.mass)
        #Sdf += ChaAF

        #Mt = self.momentum + circleB.momentum
        #self.velocity_final = ((Mt/2)/ Sm)* (90- ChaA_final)/90
        #Mt = self.kinetic_energy + circleB.kinetic_energy
        #self.velocity_final = ((Mt/2)/ )* (90- ChaA_final)/90
        #SvX = (self.velocity * cos(radians(self.direction)))
        #SvY = (self.velocity * sin(radians(self.direction)))
        #SbX = (circleB.velocity * cos(radians(circleB.direction)))
        #SbY = (circleB.velocity * sin(radians(circleB.direction)))
        
        
        
        #Sdf = round(Sdf,2)
        self.direction = Sdf
        self.last_collision = circleB
        if self == circle1:
            print("collision occured")
        #self.colour = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        



    def circle_collision_wall(self, circleA, Xb, Yb ):
        Xa = circleA.centre[0]
        Ya = circleA.centre[1]
        Sd = circleA.direction
        Bd = 0
        if Xa < Xb:
            Bd = 180
        elif Xa > Xb:
            Bd = 0
        else:
            if Ya > Yb:
                Bd = 90
            elif Ya < Yb:
                Bd = -90
        Sdf = ( 2*Bd - Sd -180)
        Sdf = Sdf % 360
        Sdf = round(Sdf,2)
        self.direction = Sdf
  
def Collision_scan_wall(circleA):
    if circleA.centre[0] <= circleA.radius and circleA.last_collision is not "Left":
        circleA.circle_collision_wall(circleA, 0, circleA.centre[1])
        circleA.last_collision = "Left"
    elif circleA.centre[0] >= WIDTH - circleA.radius and circleA.last_collision is not "Right":
        circleA.circle_collision_wall(circleA, WIDTH, circleA.centre[1] )
        circleA.last_collision = "Right"
    elif circleA.centre[1] <= circleA.radius and circleA.last_collision is not "Top":
        circleA.circle_collision_wall(circleA, circleA.centre[0], 0)
        circleA.last_collision = "Top"
    elif circleA.centre[1] >= HEIGHT - circleA.radius and circleA.last_collision is not "Bottom":
        circleA.circle_collision_wall(circleA, circleA.centre[0], HEIGHT)
        circleA.last_collision = "Bottom"
    

def Collision_scan(circleA, circleB ):
    Sum_Raduis = (circleA.radius + circleB.radius)
    Distance = sqrt((circleA.centre[0] - circleB.centre[0])**2 + (circleA.centre[1] - circleB.centre[1])**2)
    if Sum_Raduis >= Distance:
        circleA.circle_collision(circleB)
   

mouse = pygame.mouse.get_pos()
mouseX = float(mouse[0])
mouseY = float(mouse[1])
RectSizeWidth = 90
RectSizeHeight = 90
Rect1 = pygame.Rect( 0 , 0, RectSizeWidth, RectSizeHeight )

20
circle1 = Sircle([100,80,80], [600,200], 10, 5, 10, 10)
circle2 = Sircle([80,80,100], [250,300], 100, 5, 170, 10)
circle3 = Sircle([80,80,100], [300,700], 20, 5, 240, 10)
circle4 = Sircle([80,80,100], [1400,200], 20, 5, 180, 10)
circle5 = Sircle([80,80,100], [1300,200], 20, 5, 37, 10)
circle6 = Sircle([80,80,100], [1200,200], 20, 5, 61, 10)
circle7 = Sircle([80,80,100], [1100,200], 20, 5, 194, 10)
circle8 = Sircle([80,80,100], [1000,200], 20, 5, 285, 10)
circle9 = Sircle([80,80,100], [900,200], 20, 5, 346, 10)
circle10 = Sircle([80,80,100], [800,200], 20, 5, 244, 10)
Circle_List = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10]

for i in range(0):
    Circle_List.append(Sircle([100,80,80], [random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)], 20, 5, 1000, 10))

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    mouse = pygame.mouse.get_pos()
    mouseX, mouseY = mouse
    screen.fill((40, 50, 60))
    for circleNumber in Circle_List:
        for circleNumberBeta in Circle_List:
            if circleNumber is not circleNumberBeta:
                if circleNumberBeta.last_collision is not circleNumber or circleNumber.last_collision is not circleNumberBeta:
                    Collision_scan(circleNumber, circleNumberBeta)
        Collision_scan_wall(circleNumber)
    for circleNumber in Circle_List:
        circleNumber.velocity = circleNumber.velocity_final
    for circleNumber in Circle_List:
        circleNumber.circle_displacement()
        circleNumber.draw_circle()
    circle1.centre[0] = mouseX 
    circle1.centre[1] = mouseY 
    pygame.draw.rect( screen, (100, 50, 0), Rect1 )
    pygame.display.update()
    
    