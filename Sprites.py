import pygame
from Settings import *
from os import path
from Tilemap import collide_hit_rect

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        self.game_folder = path.dirname(__file__)
        self.facing = "DOWN"

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
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0,0)
        self.pos = vec(x,y)

    def get_keys(self):

        self.vel = vec(0,0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            self.facing = "LEFT"

            self.vel.x = -PLAYER_SPEED
            self.pimg = pygame.transform.flip(self.eimgs[self.index], 1, 0)
            self.index += 1

            if self.index >= len(self.eimgs):

                self.index = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            self.facing = "RIGHT"

            self.vel.x = PLAYER_SPEED
            self.pimg = self.eimgs[self.index]
            self.index += 1

            if self.index >= len(self.eimgs):

                self.index = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:

            self.facing = "UP"

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

            self.facing = "DOWN"

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

        if keys[pygame.K_e]:

            self.game.interact(self.facing)
            
    def collides_with_solid(self, dir):

        if dir == 'x':

            hits = pygame.sprite.spritecollide(self, self.game.solid, False, collide_hit_rect)
            
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0

                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2.0

                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x

        if dir == 'y':

            hits = pygame.sprite.spritecollide(self, self.game.solid, False, collide_hit_rect)

            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0

                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2.0

                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def load_anims(self):

        player_img_dir = path.join(self.game_folder, "images\\Chars\\Player")

        i = 0

        for i in range(ANIM_FRAMES - 1):
 
            self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'E_Walk\\e_walk_' + str(i) + '.png')).convert_alpha())
        
            self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'N_Walk\\n_walk_' + str(i) + '.png')).convert_alpha())

            self.neimgs.append(pygame.image.load(path.join(player_img_dir, 'NE_Walk\\ne_walk_' + str(i) + '.png')).convert_alpha())

            self.seimgs.append(pygame.image.load(path.join(player_img_dir, 'SE_Walk\\se_walk_' + str(i) + '.png')).convert_alpha())

            self.simgs.append(pygame.image.load(path.join(player_img_dir, 'S_Walk\\s_walk_' + str(i) + '.png')).convert_alpha())

    def can_interact(self, game):

        within_range = pygame.sprite.spritecollide(self, self.game.interactive, False, collide_hit_rect)

        if within_range:

            return True

    def update(self):

        self.get_keys()
        self.image = pygame.transform.scale(self.pimg, (128, 128))

        self.pos += self.vel * self.game.dt

        self.hit_rect.centerx = self.pos.x
        self.collides_with_solid('x')
        self.hit_rect.centery = self.pos.y
        self.collides_with_solid('y')
        self.rect.center = self.hit_rect.center

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, game, x, y, w, h):
        self.groups = game.walls, game.solid

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls, game.solid

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.scale(game.wall_img, (128,128))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class BG(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bg

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.scale(game.bg_img, (128,128))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Interaction_Box(pygame.sprite.Sprite):

    def __init__(self, game, x, y, w, h):

        self.groups = game.interactive

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class NPC(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.npc, game.solid
        pygame.sprite.Sprite.__init__(self, self.groups)

        game_folder = path.dirname(__file__)
        npc_img_dir = path.join(game_folder, "images\\Chars\\NPC")
        NPC_img = pygame.image.load(path.join(npc_img_dir, 'npc.gif')).convert_alpha()
        
        self.game = game
        self. image = pygame.transform.scale(NPC_img, (128,128))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y