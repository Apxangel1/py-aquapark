from abc import ABC


class IntegerRange:

    def __init__(self, min_amount : int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner: any, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance: any, owner: any) -> int:
        return getattr(instance, self.private_name)

    def __set__(self, instance: any, value: int) -> None:
        if not (self.min_amount <= value <= self.max_amount):
            raise ValueError(
                f"Number should be in range of {self.min_amount}"
                f" and {self.max_amount}!"
            )
        setattr(instance, self.private_name, value)


class Visitor:

    def __init__(self, name: str, age: int, weight: int, height: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):

    def __init__(self, age: int, weight: int, height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):

    age = IntegerRange(4, 14)
    weight = IntegerRange(20, 50)
    height = IntegerRange(80, 120)

    def __init__(self, age: int, weight: int, height: int) -> None:
        super().__init__(age, weight, height)


class AdultSlideLimitationValidator(SlideLimitationValidator):

    age = IntegerRange(14, 60)
    weight = IntegerRange(50, 120)
    height = IntegerRange(120, 220)

    def __init__(self, age: int, weight: int, height: int) -> None:
        super().__init__(age, weight, height)


class Slide:

    def __init__(self, name: str, limitation_class: any) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: "Visitor") -> bool:

        # Code that might raise an exception
        try:
            self.limitation_class(visitor.age, visitor.weight, visitor.height)

        # Handle the specific error
        except ValueError or TypeError as e:
            print(e)
            return False

        return True
