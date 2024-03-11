from abc import ABC, abstractmethod
from typing import List


class Model(ABC):
    @abstractmethod
    def generate(self, prompt: str, num_samples: int = 1, **kwargs) -> List[str]:
        pass


class ImageGenerationModel(Model, ABC):
    @abstractmethod
    def generate(self, prompt: str, neg_prompt: str = "", seed: int = 42, width: int = 512, height: int = 512,
                 scale: float = 7.0, num_samples: int = 1, num_steps: int = 20, **kwargs) -> List[str]:
        pass
