from typing import List

import numpy as npy
from PIL import Image

from src.app.service.references import BASE_DIR
from src.base.model import Model


class RandomNoiseText2ImageModel(Model):
    def generate(self, uid: str, prompt: str, neg_prompt: str = "", seed: int = 42, width: int = 512, height: int = 512,
                 scale: float = 7.0, num_samples: int = 1, **kwargs) -> List[str]:
        seed = int(seed + hash(prompt) - scale * hash(neg_prompt)) & 0xffffffff
        npy.random.seed(seed)
        folder = BASE_DIR.joinpath("output")
        if not folder.is_dir():
            folder.mkdir()
        results = []
        for i in range(num_samples):
            img = npy.uint8(npy.random.randint(0, 256, size=(height, width, 3)))
            filename = uid + "_" + str(i) + ".png"
            results.append(filename)
            Image.fromarray(img).save(folder.joinpath(filename))
        return results


if __name__ == "__main__":
    model = RandomNoiseText2ImageModel()
    print(model.generate("1", "masterpiece, best quality"))
