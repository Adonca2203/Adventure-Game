import pygame
from Settings import *
from os import path

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        game_folder = path.dirname(__file__)

        player_img_dir = path.join(game_folder, "images\\Chars\\Player")

        self.simgs = []
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_0.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_1.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_2.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_3.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_4.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_5.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_6.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_7.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_8.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_9.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_10.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_11.png')).convert_alpha())
        self.simgs.append(pygame.image.load(path.join(player_img_dir, 's_walk_12.png')).convert_alpha())
        
        self.eimgs = []
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_0.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_1.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_2.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_3.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_4.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_5.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_6.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_7.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_8.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_9.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_10.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_11.png')).convert_alpha())
        self.eimgs.append(pygame.image.load(path.join(player_img_dir, 'e_walk_12.png')).convert_alpha())
        
        self.nimgs = []
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_0.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_1.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_2.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_3.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_4.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_5.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_6.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_7.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_8.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_9.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_10.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_11.png')).convert_alpha())
        self.nimgs.append(pygame.image.load(path.join(player_img_dir, 'n_walk_12.png')).convert_alpha())


        self.index = 0

        self.pimg = self.simgs[self.index]

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = pygame.transform.scale(self.pimg, (64, 64))
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE

    def get_keys(self):

        self.vel = vec(0,0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            self.vel.x = -PLAYER_SPEED

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

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            self.vel.y = PLAYER_SPEED
            self.pimg = self.simgs[self.index]
            self.index += 1

            if self.index >= len(self.simgs):

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

    def update(self):

        self.get_keys()
        self.image = pygame.transform.scale(self.pimg, (64, 64))

        self.pos += self.vel * self.game.dt

        self.rect.x = self.pos.x
        self.collides_with_solid('x')
        self.rect.y = self.pos.y
        self.collides_with_solid('y')

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls, game.solid
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.scale(game.wall_img, (64,64))
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
        self. image = pygame.transform.scale(game.NPC_img, (64,64))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE