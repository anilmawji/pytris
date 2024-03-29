DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 750

PLAY_WIDTH = 300
PLAY_HEIGHT = 600

COLUMNS = 10
ROWS = 20

TOP_LEFT_X = (DISPLAY_WIDTH - PLAY_WIDTH) // 2
TOP_LEFT_Y = DISPLAY_HEIGHT - PLAY_HEIGHT

BLOCK_WIDTH = PLAY_WIDTH // COLUMNS
BLOCK_HEIGHT = PLAY_HEIGHT // ROWS

DEFAULT_FALL_SPEED = 0.27

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)

S = [['.00',
      '00.'],

     ['.0.',
      '.00',
      '..0']]

Z = [['00.',
      '.00'],

     ['.0',
      '00',
      '0.']]

I = [['.0',
      '.0',
      '.0',
      '.0'],

     ['0000']]

O = [['.00',
      '.00']]

J = [['0..',
      '000'],

     ['.00',
      '.0.',
      '.0.'],

     ['000',
      '..0'],

     ['.0',
      '.0',
      '00']]

L = [['..0',
      '000'],

     ['.0.',
      '.0.',
      '.00'],

     ['000',
      '0..'],

     ['00',
      '.0',
      '.0']]

T = [['.0..',
      '000.',
      '....'],

     ['.0..',
      '.00.',
      '.0..'],

     ['....',
      '000.',
      '.0..'],

     ['.0..',
      '00..',
      '.0..']]

SHAPES = [S, Z, I, O, J, L, T]
SHAPE_COLORS = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
