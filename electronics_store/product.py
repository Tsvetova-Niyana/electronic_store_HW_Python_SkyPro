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


class Product:
    """
    Создайте два атрибута класса:

    - для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
    - для хранения созданных экземпляров класса
    """
    pay_rate = 1
    product_all = []

    def __init__(self, name_product: str, amount_product: float, count_product: int, **kwargs):
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
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"Product('{self.name_product}', {self.amount_product}, {self.count_product})"

    def __str__(self):
        return self.name_product

    def __add__(self, other):
        """Реализуйте также возможность сложения экземпляров класса Phone и Product.
        Сложение идет по количеству товара в магазине.
        Реализуйте проверки, чтобы нельзя было сложить Phone или Item с экземплярами не Phone или Product классов.
        Т.е. с объектами других классов запрещено сложение."""

        if isinstance(other, Product):
            return self.count_product + other.count_product
        else:
            raise TypeError("Объекты должны относится к классам Product и/или Phone")

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
        Метод считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла items.cvs

        Используйте статический метод определения целого числа в методе класса, описанного выше, при создании
        экземпляров класса из csv-файла следующим образом: если цена или количество товара в csv-файле было
        в виде 7.0 (т.е. 0 десятых), то в соответствующие атрибуты экземпляра класса запишется число типа int (т.е. 7).
        """

        with open(file_name, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:

                amount = float(row["price"])
                product_count = float(row["quantity"])

                if cls.is_integer(amount) and cls.is_integer(product_count):
                    cls(row["name"], int(amount), int(product_count))
                elif cls.is_integer(amount):
                    cls(row["name"], int(amount), product_count)
                elif cls.is_integer(product_count):
                    cls(row["name"], amount, int(product_count))
                else:
                    cls(row["name"], amount, product_count)

    @staticmethod
    def is_integer(number) -> bool:
        """Реализуйте статический метод, который проверяет, является ли число (например, полученное из csv-файла) целым.
        Число 7.0, согласно этому методу, также является целым. Число 7.5 - нет. """
        if isinstance(number, int):
            return True
        else:
            return number.is_integer()
