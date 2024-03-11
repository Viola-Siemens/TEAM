import base64
import io
from typing import List

import numpy as npy
from PIL import Image

from src.app.service.references import BASE_DIR
from src.base.model import ImageGenerationModel


class RandomNoiseText2ImageModel(ImageGenerationModel):
    def generate(self, prompt: str, neg_prompt: str = "", seed: int = 42, width: int = 512, height: int = 512,
                 scale: float = 7.0, num_samples: int = 1, **kwargs) -> List[str]:
        seed = int(seed + hash(prompt) - scale * hash(neg_prompt)) & 0xffffffff
        npy.random.seed(seed)
        images = []
        for i in range(num_samples):
            img = npy.uint8(npy.random.randint(0, 256, size=(height, width, 3)))
            image_data = io.BytesIO()
            Image.fromarray(img).save(image_data, format="PNG")
            encoded = base64.b64encode(image_data.getvalue()).decode('utf-8')
            images.append(encoded)
        return images


if __name__ == "__main__":
    folder = BASE_DIR.joinpath("output")
    if not folder.is_dir():
        folder.mkdir()

    model = RandomNoiseText2ImageModel()
    images = model.generate("masterpiece, best quality")

    cnt = 0
    for img in images:
        filename = "1_" + str(cnt) + ".png"
        cnt += 1
        Image.open(io.BytesIO(base64.b64decode(img))).save(folder.joinpath(filename))