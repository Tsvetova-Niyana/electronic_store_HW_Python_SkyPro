"""
Создайте класс для представления товара в магазине. Экземпляр класса должен содержать атрибуты:

- название товара
- цена за единицу товара
- количество товара в магазине

Создайте два атрибута класса:

- для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
- для хранения созданных экземпляров класса

Реализуйте методы, позволяющие:

- получить общую стоимость конкретного товара в магазине
- применить установленную скидку для конкретного товара
"""
import csv
import os


class Product:
    """
    Создайте два атрибута класса:

    - для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
    - для хранения созданных экземпляров класса
    """
    pay_rate = 1
    product_all = []

    def __init__(self, name_product: str, amount_product: float, count_product: int):
        """
        Экземпляр класса должен содержать атрибуты:

        - название товара
        - цена за единицу товара
        - количество товара в магазине

        Сделайте название товара приватным атрибутом
        """

        self.__name_product = name_product
        self.amount_product = amount_product
        self.count_product = count_product

        self.product_all.append(self)

    def calculate_total_price(self):
        total_price = self.count_product * self.amount_product
        return total_price

    def apply_discount(self):
        self.amount_product = self.amount_product * self.pay_rate

    @property
    def name_product(self) -> str:
        """Возвращаем значение name_product в формате свойства"""
        return self.__name_product

    @name_product.setter
    def name_product(self, name: str) -> None:
        """Реализуйте проверку, что при задании названия товара длина его не превышает 10 символов.
            При привышении должно выбрасываться исключение."""
        if (len(name) > 10):
            raise ValueError("Название продукта не должно превышать 10 символов")
        else:
            self.__name_product = name

    @classmethod
    def create_product_by_file(cls, file_name):
        """Реализуйте метод класса, выполняющий альтернативный способ создания объектов-товаров.
        Метод считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла items.cvs"""

        with open(file_name, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                new_product = Product(row["name"], row["price"], row["quantity"])

    def __repr__(self) -> str:
        return self.name_product
