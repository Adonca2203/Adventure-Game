import pygame
from Settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = pygame.Surface((TILESIZE/1.5, TILESIZE/1.5))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.vx, self.vy = 0, 0

    def get_keys(self):

        self.vx, self.vy = 0, 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            self.vx = -PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            self.vx = PLAYER_SPEED

        if keys[pygame.K_UP] or keys[pygame.K_w]:

            self.vy = -PLAYER_SPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            self.vy = PLAYER_SPEED

        if self.vx != 0 and self.vy != 0:

            self.vx *= 0.7071
            self.vy *= 0.7071
            
    def collides_with_solid(self, dir):

        if dir == 'x':

            hits = pygame.sprite.spritecollide(self, self.game.solid, False)
            
            if hits:

                if self.vx > 0:

                    self.x = hits[0].rect.left - self.rect.width

                if self.vx < 0:

                    self.x = hits[0].rect.right

                self.vx = 0
                self.rect.x = self.x

        if dir == 'y':

            hits = pygame.sprite.spritecollide(self, self.game.solid, False)

            if hits:

                if self.vy > 0:

                    self.y = hits[0].rect.top - self.rect.height

                if self.vy < 0:

                    self.y = hits[0].rect.bottom

                self.vy = 0
                self.rect.y = self.y

    def update(self):

        self.get_keys()

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collides_with_solid('x')
        self.rect.y = self.y
        self.collides_with_solid('y')

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y, wall_img):
        self.groups = game.all_sprites, game.walls, game.solid
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.transform.scale(wall_img, (32,32))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class NPC(pygame.sprite.Sprite):

    def __init__(self, game, x, y, npc_img):

        self.groups = game.all_sprites, game.npc, game.solid
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self. image = pygame.transform.scale(npc_img, (32,32))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
