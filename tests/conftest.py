import pytest
import pygame
from environs import Env

env = Env()
env.read_env()


@pytest.fixture()
def init_pygame():
    pygame.init()
    yield
    pygame.quit()
