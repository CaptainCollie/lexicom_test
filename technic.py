import functools


# def decorator(cls):
#     cls.__lt__ = lambda self, other: len(self.name) < len(other.name)
#     cls.__eq__ = lambda self, other: len(self.name) == len(other.name)
#     return functools.total_ordering(cls)


# @decorator
@functools.total_ordering
class Technic:
    __slots__ = ["name", "price", "presence", "category"]

    def __init__(self, name: str, price: int, presence: bool):
        self.name = name
        self.price = price
        self.presence = presence
        self.category = "Бюджетный" if price < 100000 else "Дорогой"

    def __lt__(self, other):
        if not isinstance(other, Technic):
            raise NotImplemented
        return len(self.name) < len(other.name)

    def __eq__(self, other):
        if not isinstance(other, Technic):
            raise NotImplemented
        return len(self.name) == len(other.name)
