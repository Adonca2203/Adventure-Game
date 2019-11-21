# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Adventure Game"
BGCOLOR = DARKGREY

# screen settings
TILESIZE = 128
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# world settings

WALL_IMG = "wall.png"
NPC_IMG = "npc.gif"
BG_IMG = "grass.png"

# player settings
PLAYER_SPEED = 350
PLAYER_IMG = "s_walk_0.png"
ANIM_FRAMES = 60