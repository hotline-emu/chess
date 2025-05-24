from environs import Env
from chess.game.instance import Instance

if __name__ == "__main__":
    env = Env()
    env.read_env()
    config = {
        "tile_size": env.int("tile_size"),
        "framerate": env.int("framerate"),
        "scale_multiplier": env.int("scale_multiplier"),
    }

    with Instance(config) as instance:
        instance.run()
