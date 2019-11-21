import pygame
from Settings import *
from os import path

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        self.game_folder = path.dirname(__file__)

        self.simgs = []
        self.eimgs = []
        self.nimgs = []
        self.neimgs = []
        self.seimgs = []

        self.load_anims()

        self.index = 0

        self.pimg = self.simgs[self.index]

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = pygame.transform.scale(self.pimg, (128, 128))
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE

    def get_keys(self):

        self.vel = vec(0,0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            self.vel.x = -PLAYER_SPEED
            self.pimg = pygame.transform.flip(self.eimgs[self.index], 1, 0)
            self.index += 1

            if self.index >= len(self.eimgs):

                self.index = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            self.vel.x = PLAYER_SPEED
            self.pimg = self.eimgs[self.index]
            self.index += 1

            if self.index >= len(self.eimgs):

                self.index = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:

            self.vel.y = -PLAYER_SPEED
            self.pimg = self.nimgs[self.index]
            self.index += 1

            if self.index >= len(self.nimgs):

                self.index = 0

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):

            self.pimg = self.neimgs[self.index]
            self.index += 1

            if self.index >= len(self.neimgs):

                self.index = 0

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):

            self.pimg = pygame.transform.flip(self.neimgs[self.index], 1, 0)
            self.index += 1

            if self.index >= len(self.neimgs):

                self.index = 0

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            self.vel.y = PLAYER_SPEED
            self.pimg = self.simgs[self.index]
            self.index += 1

            if self.index >= len(self.simgs):

                self.index = 0

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):

            self.pimg = self.seimgs[self.index]
            self.index += 1

            if self.index >= len(self.seimgs):

                self.index = 0

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):

            self.pimg = pygame.transform.flip(self.seimgs[self.index], 1, 0)
            self.index += 1

            if self.index >= len(self.seimgs):

                self.index = 0

        if self.vel.x != 0 and self.vel.y != 0:

            self.vel *= 0.7071
            
    def collides_with_solid(self, dir):

        if dir == 'x':

            hits = pygame.sprite.spritecollide(self, self.game.solid, False)
            
            if hits:

                if self.vel.x > 0:

                    self.pos.x = hits[0].rect.left - self.rect.width

                if self.vel.x < 0:

                    self.pos.x = hits[0].rect.right

                self.vel.x = 0
                self.rect.x = self.pos.x

        if dir == 'y':

            hits = pygame.sprite.spritecollide(self, self.game.solid, False)

            if hits:

                if self.vel.y > 0:

                    self.pos.y = hits[0].rect.top - self.rect.height

                if self.vel.y < 0:

                    self.pos.y = hits[0].rect.bottom

                self.vel.y = 0
                self.rect.y = self.pos.y

    def load_anims(self):

        player_img_dir = path.join(self.game_folder, "images\\Chars\\Player")

        i = 0

        for i in range(ANIM_FRAMES):
 
            self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'E_Walk\\e_walk_' + str(i) + '.png')).convert_alpha())
        
            self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'N_Walk\\n_walk_' + str(i) + '.png')).convert_alpha())

            self.neimgs.append(pygame.image.load(path.join(player_img_dir, 'NE_Walk\\ne_walk_' + str(i) + '.png')).convert_alpha())

            self.seimgs.append(pygame.image.load(path.join(player_img_dir, 'SE_Walk\\se_walk_' + str(i) + '.png')).convert_alpha())

            self.simgs.append(pygame.image.load(path.join(player_img_dir, 'S_Walk\\s_walk_' + str(i) + '.png')).convert_alpha())

    def update(self):

        self.get_keys()
        self.image = pygame.transform.scale(self.pimg, (128, 128))

        self.pos += self.vel * self.game.dt

        self.rect.x = self.pos.x
        self.collides_with_solid('x')
        self.rect.y = self.pos.y
        self.collides_with_solid('y')

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y, solid = 1):
        self.groups = game.all_sprites, game.walls

        if solid:

            self.groups = game.solid

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.scale(game.bg_img, (128,128))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class NPC(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.npc, game.solid
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self. image = pygame.transform.scale(game.NPC_img, (128,128))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE