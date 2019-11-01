import pygame
import random
import sys
from os import path
from Settings import *
from Sprites import *

walls_img_dir = path.join(path.dirname(__file__), "images\\Wall")
npc_img_dir = path.join(path.dirname(__file__), "images\\Chars\\NPC")

wall_img = pygame.image.load(path.join(walls_img_dir, "wall.png"))
NPC_img = pygame.image.load(path.join(npc_img_dir, "npc.gif"))

class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500,100)
        self.load_data()

    def load_data(self):

        game_folder = path.dirname(__file__)
        self.map_data = []

        with open(path.join(game_folder, 'map.txt'), 'rt') as f:

            for line in f:

                self.map_data.append(line)

    def new(self):

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.solid = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        
        for row, tiles in enumerate(self.map_data):

            for col, tile in enumerate(tiles):

                if tile == '1':

                    Wall(self, col, row, wall_img)

                if tile == '3':

                    NPC(self, col, row, NPC_img)


    def run(self):

        self.playing = True

        while self.playing:

            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):

            pygame.quit()
            sys.exit()

    def update(self):

            self.all_sprites.update()

    def draw_grid(self):

            for x in range(0, WIDTH, TILESIZE):

                pygame.draw.line(self.screen, LIGHTGREY, (x,0), (x, HEIGHT))

            for y in range(0, HEIGHT, TILESIZE):

                pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):

        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    
                    self.quit()

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    
                    self.player.move(dx=-1)

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    
                    self.player.move(dx=1)

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    
                    self.player.move(dy=1)

                if event.key == pygame.K_w or event.key == pygame.K_UP:

                    self.player.move(dy=-1)

    def show_start_screen(self):

        pass

g = Game()

while True:

    g.new()
    g.run()