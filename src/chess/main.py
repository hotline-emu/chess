from environs import Env
from .game_instance import GameInstance

if __name__ == "__main__":
    env = Env()
    env.read_env()
    config = {
        "tile_size": env.int("tile_size"),
        "framerate": env.int("framerate"),
        "scale_multiplier": env.int("scale_multiplier"),
    }

    with GameInstance(config) as instance:
        instance.run()
