import pygame
from environs import Env
from chess.game import ChessGame


def main() -> None:
    env = Env()
    env.read_env()
    pygame.init()
    board_size = env.int("tile_size") * env.int("board_size_multiplier")
    screen = pygame.display.set_mode((board_size, board_size))
    clock = pygame.time.Clock()
    game = ChessGame(screen)

    running = True
    while running:
        fps = env.int("fps")
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update()
        game.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
