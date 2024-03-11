from typing import List

from src.base.model import Model


class M2UGenText2MusicModel(Model):
    API_ADDRESS: str = "http://127.0.0.1:7860/sdapi/v1/img2img"

    def generate(self, prompt: str, num_samples: int = 1, **kwargs) -> List[str]:
        # TODO
        pass
