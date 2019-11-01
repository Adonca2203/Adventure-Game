import pygame
from Settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self. image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):

        if not self.collides_with_solid(dx, dy):
            self.x += dx
            self.y += dy

    def collides_with_solid(self, dx=0, dy=0):

        for solid in self.game.solid:

            if solid.x == self.x + dx and solid.y == self.y + dy:

                return True

        return False

    def update(self):

        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

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
