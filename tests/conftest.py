from typing import Iterator
import pytest
import pygame
from environs import Env

env = Env()
env.read_env()


@pytest.fixture()
def init_pygame() -> Iterator[None]:
    pygame.init()
    yield
    pygame.quit()
