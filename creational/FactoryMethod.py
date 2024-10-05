from __future__ import annotations
from abc import ABC, abstractmethod


class Creator:

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class ConcreteCreatorOne(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductOne()


class ConcreteCreatorTwo(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductTwo()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductOne(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProductOne}"


class ConcreteProductTwo(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProductTwo}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorOne.")
    client_code(ConcreteCreatorOne())
    print("\n")

    print("App: Launched with the ConcreteCreatorTwo.")
    client_code(ConcreteCreatorTwo())
