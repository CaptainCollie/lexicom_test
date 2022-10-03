from Tasks.tasks1.task import optimize_saving
from Tasks.tasks2.task import make_file_names


def test_optimize_saving():
    technic = [
        ("Ноутбук", 1500, "Татьяна", "89002001020"),
        ("Смартфон", 500, "Анна", "89202202325"),
        ("Проектор", 300, "Андрей", "89505205656"),
        ("Принтер", 750, "Игорь", "89303303236"),
        ("Планшет", 2300, "Игорь", "89303303236"),
        ("Смартфон", 1000, "Андрей", "89505205656"),
        ("Ноутбук", 4800, "Татьяна", "89002001020"),
        ("Наушники", 780, "Марина", "89562002350"),
        ("Сканер", 550, "Сергей", "89808564559"),
        ("Планшет", 1200, "Анна", "89202202325"),
        ("Ноутбук", 1100, "Игорь", "89303303236"),
        ("Смартфон", 3500, "Татьяна", "89002001020"),
    ]
    optimized_technic = optimize_saving(technic)
    for buyer in optimized_technic:
        print(buyer)

    """
    Татьяна 89002001020: Ноутбук - 1500; Ноутбук - 4800; Смартфон - 3500
    Анна 89202202325: Смартфон - 500; Планшет - 1200
    Андрей 89505205656: Проектор - 300; Смартфон - 1000
    Игорь 89303303236: Принтер - 750; Планшет - 2300; Ноутбук - 1100
    Марина 89562002350: Наушники - 780
    Сергей 89808564559: Сканер - 550
    """


def test_make_file_names():
    file_names = [
        "first",
        "longest",
        "nnnnn",
        ""
    ]
    file_names = make_file_names(file_names)
    assert file_names == [
        "first__",
        "longest",
        "n______",
        "_______"
    ]


if __name__ == '__main__':
    test_optimize_saving()
    test_make_file_names()
