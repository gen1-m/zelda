import pygame

title = "Zelda Laby"
image_icon = "images/link_right.gif"
image_intro = "images/intro.jpg"
image_back = "images/back.jpg"
image_wall = "images/wall.gif"
image_start = "images/thumb_Hole.gif"
image_triforce = "images/triforce.gif"

nb_sprite = 15
sprite_size = 30
window_size = nb_sprite * sprite_size

pygame.init()

window = pygame.display.set_mode((640, 480))
icon = pygame.image.load("images/link_right.gif")

class Perso:
    def __init__(self, right, left, up, down, map):
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()

        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        self.direction = self.down
        self.map = map
    def move(self, direction):
        if direction == 'right':
            if self.case_x < (nb_sprite - 10):
                if self.map.structure[self.case_y][self.case_x+10] != 'L':
                    self.case_x += 10
                    self.x = self.case_x * sprite_size
                    self.direction = self.right
        if direction == 'left':
            if self.case_x < (nb_sprite - 10):
                if self.map.structure[self.case_y][self.case_x-10] != 'L':
                    self.case_x += 10
                    self.x = self.case_x * sprite_size
                    self.direction = self.left
        if direction == 'up':
            if self.case_y < (nb_sprite - 10):
                if self.map.structure[self.case_y+10][self.case_x] != 'L':
                    self.case_y += 10
                    self.y = self.case_y * sprite_size
                    self.direction = self.up
        if direction == 'down':
            if self.case_y < (nb_sprite - 10):
                if self.map.structure[self.case_y-10][self.case_x] != 'L':
                    self.case_y += 10
                    self.y = self.case_y * sprite_size
                    self.direction = self.down

class Map:
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def show (self, window):
        wall = pygame.image.load(image_wall).convert()
        start = pygame.image.load(image_start).convert()
        triforce = pygame.image.load(image_triforce).convert_alpha()

        nb_line = 0
        for line in self.structure:
           nb_pos = 0
        for sprite in line:
            x = nb_pos * sprite_size
            y = nb_line * sprite_size
        if sprite == 'W':
            window.blit(wall, (x,y))
        elif sprite == 'L':
            window.blit(start, (x,y))
        elif sprite == 'T':
            window.blit(triforce, (x,y))
        nb_pos = nb_pos + 1
        nb_line = nb_line + 1

    def create(self):
        with open(self.file, "r") as file:
            structure_map = []
            for line in file:
                map_line = []
                for sprite in line:
                    map_line.append(sprite)
                    structure_map.append(map_line)
                    self.structure = structure_map               


loop = 1
while loop:
    intro = pygame.image.load("images/intro.jpg").convert()
    window.blit(intro, (0,0))
    pygame.display.flip()

    loop_intro = 1
    loop_game = 1

    while loop_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or  \
            event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE:
                loop_intro = 0
                loop_game = 0
                loop = 0
                load_map = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    loop_intro = 0
                    load_map = "LinkToThePast"
                if load_map != 0:
                    back = pygame.image.load("images/back.jpg").convert()
                    map = Map(load_map)
                    map.create()
                    map.show(window)
                    link = Perso("images/link_right.gif", "images/link_left.gif", "images/link_up.gif", "images/link_down.gif", map)
                    if event.key == pygame.K_RIGHT:
                        link.move("right")
                    if event.key == pygame.K_LEFT:
                        link.move("left")
                    if event.key == pygame.K_UP:
                        link.move("up")
                    if event.key == pygame.K_DOWN:
                        link.move("down")

                    window.blit(back, (0,0))
                    map.show(window)
                    window.blit(link.direction, (link.x, link.y))
                    pygame.display.flip()







