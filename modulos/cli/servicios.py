from abc import ABC
from abc import abstractmethod
from ..base.modelo import ModeloBase
import os


class CLIservicios(ABC):
    def prompt_item(self) -> ModeloBase:
        item = ModeloBase()
        return item

    def clear(self):
        os.system('clear' if os.name == 'posix' else 'cls')
