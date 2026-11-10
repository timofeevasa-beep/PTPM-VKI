from abc import ABC, abstractmethod

class IUserInput(ABC):
    @abstractmethod
    def get_sides(self) -> tuple[float, float, float]:
        pass

class IExternalService(ABC):
    @abstractmethod
    def send_result(self, data: str) -> None:
        pass