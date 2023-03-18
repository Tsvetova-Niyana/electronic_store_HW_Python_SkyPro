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
        """

        self.name_product = name_product
        self.amount_product = amount_product
        self.count_product = count_product

        self.product_all.append(self)

    def calculate_total_price(self):
        total_price = self.count_product * self.amount_product
        return total_price

    def apply_discount(self):
        self.amount_product = self.amount_product * self.pay_rate

    def __repr__(self) -> str:
        return self.name_product
