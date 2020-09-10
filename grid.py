import pygame
from constants import *


class Grid:

    def __init__(self, columns, rows):
        self.cells = [[BLACK for i in range(columns)] for i in range(rows)]
        self.columns = columns
        self.rows = rows

    def render(self, display, current_piece):
        # Draw grid cells
        for y in range(self.rows):
            for x in range(self.columns):
                pygame.draw.rect(display, self.cells[y][x],
                                 (TOP_LEFT_X + x * BLOCK_WIDTH, TOP_LEFT_Y + y * BLOCK_HEIGHT,
                                  BLOCK_WIDTH, BLOCK_HEIGHT))
        # Draw falling piece
        current_piece.render(display, self)

        # Draw vertical lines
        for x in range(self.columns):
            pygame.draw.line(display, GRAY, (TOP_LEFT_X + x * BLOCK_WIDTH, DISPLAY_HEIGHT - PLAY_HEIGHT),
                             (TOP_LEFT_X + x * BLOCK_WIDTH, DISPLAY_HEIGHT))
        # Draw horizontal lines
        for y in range(self.rows):
            pygame.draw.line(display, GRAY, (TOP_LEFT_X, DISPLAY_HEIGHT - PLAY_HEIGHT + y * BLOCK_HEIGHT),
                             (TOP_LEFT_X + PLAY_WIDTH, TOP_LEFT_Y + y * BLOCK_HEIGHT))
        # Draw border
        pygame.draw.rect(display, WHITE, (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 4)

    def is_valid_space(self, piece):
        for (x, y) in piece.get_segments():
            if x < 0 or x >= self.columns or y >= self.rows or (y >= 0 and self.cells[y][x] is not BLACK):
                return False
        return True

    def lock_piece(self, piece):
        for (x, y) in piece.get_segments():
            if self.cells[y][x] is not BLACK:
                return False
        for (x, y) in piece.get_segments():
            self.cells[y][x] = piece.get_color()
        return True

    def clear_lines(self):
        num_cleared = 0

        for y, line in enumerate(self.cells):
            should_clear = True
            for cell in line:
                if cell is BLACK:
                    should_clear = False
                    break
            if should_clear:
                num_cleared += 1
                self.cells[y] = [BLACK for i in range(self.columns)]
                for i, row in enumerate(self.cells[:y]):
                    self.cells[i + 1] = row
        return num_cleared

    def clear(self):
        self.cells = [[BLACK for i in range(self.columns)] for i in range(self.rows)]

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows
