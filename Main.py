import pygame
import random
import sys
from os import path
from Settings import *
from Sprites import *
from Tilemap import *


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

        walls_img_dir = path.join(game_folder, "images\\Wall")
        npc_img_dir = path.join(game_folder, "images\\Chars\\NPC")
        bg_img_dir = path.join(game_folder, "images\\BG")

        self.wall_img = pygame.image.load(path.join(walls_img_dir, WALL_IMG)).convert_alpha()
        self.NPC_img = pygame.image.load(path.join(npc_img_dir, NPC_IMG)).convert_alpha()
        self.bg_img = pygame.image.load(path.join(bg_img_dir, BG_IMG)).convert_alpha()


        self.map = Map(path.join(game_folder, 'Maps\\World_Map.txt'))

    def new(self):

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.solid = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.bg = pygame.sprite.Group()
        
        for row, tiles in enumerate(self.map.data):

            for col, tile in enumerate(tiles):

                if tile =='.':

                    BG(self, col, row, 0)

                if tile == '1':

                    Wall(self, col, row)

                if tile == '3':

                    NPC(self, col, row)

                if tile == 'P':

                    self.player = Player(self, col, row)

        self.camera = Camera(self.map.width, self.map.height)

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
            self.camera.update(self.player)

    def draw_grid(self):

            for x in range(0, WIDTH, TILESIZE):

                pygame.draw.line(self.screen, LIGHTGREY, (x,0), (x, HEIGHT))

            for y in range(0, HEIGHT, TILESIZE):

                pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):

        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:

            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pygame.display.flip()

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    
                    self.quit()

    def show_start_screen(self):

        pass

g = Game()

while True:

    g.new()
    g.run()