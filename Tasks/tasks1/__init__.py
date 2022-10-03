class Buyer:
    def __init__(self, name: str, number: str, card: list[tuple[str, int]]):
        self.name = name
        self.number = number
        self.card = card

    def add_to_card(self, product: str, price: int):
        self.card.append((product, price))

    def __str__(self):
        return f"{self.name} {self.number}: {'; '.join([f'{tech[0]} - {tech[1]}' for tech in self.card])}"


def optimize_saving(technic: list) -> list[Buyer]:
    name_number_mapping = {}

    for product, price, name, number in technic:
        name_number_mapping.setdefault((name, number),
                                       Buyer(name, number, []))
        name_number_mapping[(name, number)].add_to_card(product, price)

    technic = name_number_mapping.values()
    return list(technic)
