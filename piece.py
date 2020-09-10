import pygame
import random
from constants import *


class Piece:

    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0

    def __str__(self):
        return '\n'.join(self.get_form())

    @classmethod
    def generate_random(cls):
        return Piece(COLUMNS // 2 - 2, -4, random.choice(SHAPES))

    def render(self, display, grid):
        for (x, y) in self.get_visible_segments(grid):
            pygame.draw.rect(display, self.color, (TOP_LEFT_X + x * BLOCK_WIDTH, TOP_LEFT_Y + y * BLOCK_HEIGHT,
                                                   BLOCK_WIDTH, BLOCK_HEIGHT))

    def get_segments(self):
        positions = []

        for offset_y, row in enumerate(self.get_form()):
            for offset_x, segment in enumerate(row):
                if segment == '0':
                    positions.append((self.x + offset_x, self.y + offset_y))
        return positions

    def get_visible_segments(self, grid):
        if self.y > 0:
            return self.get_segments()

        positions = []
        for (x, y) in self.get_segments():
            if 0 <= x < grid.get_columns() and 0 <= y < grid.get_rows():
                positions.append((x, y))
        return positions

    def can_rotate(self):
        return len(self.shape) > 1

    def get_form(self):
        return self.shape[self.rotation]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color
