import base64
import io
import json
from typing import List

import requests
from PIL import Image

from src.app.service.references import BASE_DIR

from src.base.model import Model


class StableDiffusionText2ImageModel(Model):
    API_ADDRESS: str = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    api_key: str

    def generate(self, uid: str, prompt: str, neg_prompt: str = "", seed: int = 42, width: int = 512, height: int = 512,
                 scale: float = 7.0, num_samples: int = 1, num_steps: int = 20, **kwargs) -> List[str]:
        images = requests.post(url=self.API_ADDRESS, data=json.dumps({
            "prompt": prompt, "neg_prompt": neg_prompt, "seed": seed, "width": width, "height": height,
            "scale": scale, "n_iter": num_samples, "steps": num_steps
        })).json()["images"]
        cnt = 0
        results = []
        folder = BASE_DIR.joinpath("output")
        if not folder.is_dir():
            folder.mkdir()
        for img in images:
            filename = uid + "_" + str(cnt) + ".png"
            cnt += 1
            results.append(filename)
            Image.open(io.BytesIO(base64.b64decode(img))).save(folder.joinpath(filename))
        return results


# noinspection PyMethodOverriding
class StableDiffusionImage2ImageModel(Model):
    API_ADDRESS: str = "http://127.0.0.1:7860/sdapi/v1/img2img"
    api_key: str

    def generate(self, uid: str, prompt: str, input_image: str, neg_prompt: str = "", seed: int = 42,
                 width: int = 512, height: int = 512, scale: float = 7.0, num_samples: int = 1,
                 num_steps: int = 20, strength: float = 0.6, **kwargs) -> List[str]:
        images = requests.post(url=self.API_ADDRESS, data=json.dumps({
            "prompt": prompt, "neg_prompt": neg_prompt, "init_images": [input_image], "seed": seed,
            "width": width, "height": height, "scale": scale, "n_iter": num_samples,
            "steps": num_steps, "denoising_strength": strength
        })).json()["images"]
        cnt = 0
        results = []
        folder = BASE_DIR.joinpath("output")
        if not folder.is_dir():
            folder.mkdir()
        for img in images:
            filename = uid + "_" + str(cnt) + ".png"
            cnt += 1
            results.append(filename)
            Image.open(io.BytesIO(base64.b64decode(img))).save(folder.joinpath(filename))
        return results


if __name__ == "__main__":
    # model = StableDiffusionText2ImageModel()
    # print(model.generate(
    #     "1",
    #     "masterpiece, best quality, anime, a beautiful girl, long straight hair, pink hair, pink skirt, sitting "
    #     "under a tree",
    #     "nsfw, realistic, low quality, lowres, watermark, ugly, blurry, bad legs, bad hands",
    #     num_steps=50,
    #     num_samples=2
    # ))

    image = Image.open("D:\\Downloads\\f64c3eea5c1d6eba1f41d3a80eec8d6db7ba21ed.jpg")
    image_data = io.BytesIO()
    image.save(image_data, format="PNG")
    encoded = base64.b64encode(image_data.getvalue()).decode('utf-8')
    model = StableDiffusionImage2ImageModel()
    print(model.generate(
        "1",
        "masterpiece, best quality, anime, a beautiful girl, long straight hair, pink hair, pink skirt, sitting, "
        "white stockings",
        encoded,
        "nsfw, realistic, low quality, lowres, watermark, ugly, blurry, bad legs, bad hands",
        num_steps=50,
        strength=0.25,
        num_samples=2
    ))
