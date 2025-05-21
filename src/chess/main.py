import pygame
from environs import Env
from chess.game import ChessGame
from chess.config import BOARD_SIZE, FPS


def main() -> None:
    env = Env()
    env.read_env()
    pygame.init()
    screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    clock = pygame.time.Clock()
    game = ChessGame(screen)

    running = True
    while running:
        clock.tick(FPS)
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
