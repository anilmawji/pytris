import pygame
from constants import *
from piece import Piece
from grid import Grid


def render_message(display, text, size=40, color=WHITE):
    alpha_surface = pygame.Surface((PLAY_WIDTH, PLAY_HEIGHT))

    alpha_surface.set_alpha(128)
    alpha_surface.fill(GRAY)
    display.blit(alpha_surface, (TOP_LEFT_X, TOP_LEFT_Y))

    font = pygame.font.SysFont('freesansbold.ttf', size, bold=True)
    label = font.render(text, True, color)

    display.blit(label, (TOP_LEFT_X + PLAY_WIDTH // 2 - (label.get_width() // 2),
                         TOP_LEFT_Y + PLAY_HEIGHT // 2 - label.get_height() // 2))


def render_next_piece(display, piece):
    font = pygame.font.SysFont('freesansbold.ttf', 30)
    label = font.render('NEXT', True, WHITE)
    offset_x = TOP_LEFT_X + PLAY_WIDTH + (DISPLAY_WIDTH - PLAY_WIDTH) // 6
    offset_y = TOP_LEFT_Y + PLAY_HEIGHT // 2 - 200

    for y, row in enumerate(piece.get_form()):
        for x, segment in enumerate(row):
            if segment == '0':
                pygame.draw.rect(display, piece.get_color(),
                                 (offset_x + x * BLOCK_WIDTH, offset_y + y * BLOCK_HEIGHT,
                                  BLOCK_WIDTH, BLOCK_HEIGHT))
    display.blit(label, (offset_x + 10, offset_y - 40))


def render_score(display, score, high_score):
    font = pygame.font.Font('freesansbold.ttf', 18)
    score_label = font.render('SCORE: ' + str(score), True, WHITE)
    high_score_label = font.render('HIGH SCORE: ' + str(high_score), True, WHITE)

    display.blit(score_label, (TOP_LEFT_X + PLAY_WIDTH // 2 - (score_label.get_width() // 2), 80))
    display.blit(high_score_label, (TOP_LEFT_X + PLAY_WIDTH // 2 - (high_score_label.get_width() // 2), 100))


def render_title(display):
    font = pygame.font.Font('freesansbold.ttf', 50)
    title_label = font.render('PYTRIS', True, WHITE)

    display.blit(title_label, (TOP_LEFT_X + PLAY_WIDTH // 2 - (title_label.get_width() // 2), 25))


def calculate_score(lines):
    return 0 if lines == 0 else 40 if lines == 1 else 100 if lines == 2 else 300 if lines == 3 else 1200


def main():
    pygame.init()
    pygame.display.set_caption('Pytris')
    pygame.mouse.set_visible(False)

    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    grid = Grid(COLUMNS, ROWS)
    current_piece = Piece.generate_random()
    next_piece = Piece.generate_random()
    fall_time = 0
    fall_speed = DEFAULT_FALL_SPEED
    score = 0
    high_score = 0
    running = True

    while running:
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not grid.is_valid_space(current_piece):
                current_piece.y -= 1
                if grid.lock_piece(current_piece):
                    num_lines = grid.clear_lines()
                    score += calculate_score(num_lines)
                    if score > high_score:
                        high_score = score
                    current_piece = next_piece
                    next_piece = Piece.generate_random()
                else:
                    render_message(display, "GAME OVER", 50)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    score = 0
                    grid.clear()
                    current_piece = Piece.generate_random()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    current_piece.x -= 1
                    if not grid.is_valid_space(current_piece):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    current_piece.x += 1
                    if not grid.is_valid_space(current_piece):
                        current_piece.x -= 1

                if (event.key == pygame.K_UP or event.key == pygame.K_w) and current_piece.can_rotate():
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not grid.is_valid_space(current_piece):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    fall_speed = DEFAULT_FALL_SPEED / 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    fall_speed = DEFAULT_FALL_SPEED

        display.fill(BLACK)
        render_title(display)
        render_score(display, score, high_score)
        render_next_piece(display, next_piece)
        grid.render(display, current_piece)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
