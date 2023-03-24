from openai.error import InvalidRequestError
from src.logger import logger
from src.models import ModelInterface
from src.memory import MemoryInterface

class ChatGPT:
    def __init__(self, model: ModelInterface, memory: MemoryInterface):
        self.model = model
        self.memory = memory

    def get_response(self, user_id: str, text: str) -> str:
        self.memory.append(user_id, {"role": "user", "content": text})
        try:
            response = self.model.chat_completion(self.memory.get(user_id))
        except InvalidRequestError as e:
            if "This model's maximum context length is 4097 tokens." in str(e):
                self.clean_history(user_id)
                response = self.model.chat_completion(self.memory.get(user_id))
            else:
                raise e

        logger.info(response["usage"])
        role = response["choices"][0]["message"]["role"]
        content = response["choices"][0]["message"]["content"]
        self.memory.append(user_id, {"role": role, "content": content})
        return content

    def clean_history(self, user_id: str) -> None:
        """keep only the latest memory and remove the rest"""
        self.memory.clean(user_id)

    def reset_history(self, user_id: str) -> None:
        """"remove all memory"""
        self.memory.reset(user_id)


class DALLE:
    def __init__(self, model: ModelInterface):
        self.model = model

    def generate(self, text: str) -> str:
        return self.model.image_generation(text)
