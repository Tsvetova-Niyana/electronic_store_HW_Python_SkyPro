import csv
import os

from electronics_store.product import Product
import pytest

product = Product("Смартфон", 10000, 20)


class TestProduct:
    def test_check_name_at_init_product(self):
        """Проверка корректного получения наименования продукта (name_product)"""

        assert product.name_product == "Смартфон"

    def test_check_amount_product_at_init_product(self):
        """Проверка корректного получения цены продукта (amount_product)"""

        assert product.amount_product == 10000

    def test_check_count_product_at_init_product(self):
        """Проверка корректного получения количества продукта (count_product)"""

        assert product.count_product == 20

    def test_check_pay_rate_at_init_product(self):
        """Проверка корректного получения уровня скидки (pay_rate)"""

        assert product.pay_rate == 1

    def test_check_product_all_at_init_product(self):
        """Проверка корректного получения перечня всех продуктов (product_all)"""

        product_2 = Product("Ноутбук", 20000, 5)
        assert product.product_all == [product, product_2]

    def test_calculate_total_price(self):
        """Проверка корректной работы метода calculate_total_price"""

        assert product.calculate_total_price() == 200_000

    def test_change_pay_rate(self):
        """Проверка корректной работы изменения скидки (pay_rate) для класса Product"""

        Product.pay_rate = 0.85
        assert product.pay_rate == 0.85

    def test_apply_discount(self):
        """Проверка корректной работы метода apply_discount для класса Product"""

        product.apply_discount()
        assert product.amount_product == 8_500

    def test_type_name(self):
        """Проверка типа значения в поле name_product (str)"""

        assert type(product.name_product) == str

    def test_type_amount_product(self):
        """Проверка типа значения в поле amount_product (float)"""

        assert type(product.amount_product) == float

    def test_type_count_product(self):
        """Проверка типа значения в поле count_product (int)"""

        assert type(product.count_product) == int

    def test_type_pay_rate(self):
        """Проверка типа значения в поле pay_rate (float)"""

        assert type(product.pay_rate) == float

    def test_type_product_all(self):
        """Проверка типа значения в поле product_all (list)"""
        assert type(product.product_all) == list

    def test_init_exeptions(self):
        """Проверка получения ошибки при инициализации экземпляра класса Product без параметров"""

        with pytest.raises(TypeError):
            Product()

    def test_check_len_name_exeptions(self):
        """Проверка получения ошибки при присвоении наименования товара, состоящее
         из более 10 символов"""

        with pytest.raises(ValueError):
            product.name_product = "СуперНоутбук"

    def test_open_file(self):
        """Проверка открытия файла"""

        current = os.getcwd()
        folder = "electronics_store"
        full_path = os.path.join(current, folder, "items.csv")

        with open(full_path) as file:
            result = csv.DictReader(file)
        assert result is not None

    def test_create_product_by_file(self):
        """Проверка создания продуктов из файла"""

        Product.create_product_by_file('electronics_store/items.csv')
        assert len(product.product_all) == 7

    def test_check_int_by_is_integer(self):
        """Проверка корректной работы метода is_integer(целое число)"""

        assert Product.is_integer(5) is True

    def test_check_int_with_fractional_part_by_is_integer(self):
        """Проверка корректной работы метода is_integer(целое число с дробной частью)"""
        assert Product.is_integer(7.0) is True

    def test_check_float_by_is_integer(self):
        """Проверка корректной работы метода is_integer (дробное число)"""
        assert Product.is_integer(8.5) is False

    def test_check_float_amount_product_is_int(self):
        """Проверка корректной работы метода is_integer для цены продукта
        при создании продукта из файла (дробное число)"""
        Product.create_product_by_file('electronics_store/items.csv')
        assert product.product_all[3].amount_product == 1000.25

    def test_check_int_amount_product_is_int(self):
        """Проверка корректной работы метода is_integer для цены продукта
            при создании продукта из файла (целое число)"""
        Product.create_product_by_file('electronics_store/items.csv')
        assert product.product_all[6].amount_product == 75

    def test_check_int_with_factorial_amount_product_is_int(self):
        """Проверка корректной работы метода is_integer для цены продукта
            при создании продукта из файла (целое число с дробной частью)"""

        Product.create_product_by_file('electronics_store/items.csv')
        assert product.product_all[2].amount_product == 100

    def test_check_float_count_is_int(self):
        """Проверка корректной работы метода is_integer для количества продукта
            при создании продукта из файла (дробное число)"""

        Product.create_product_by_file('electronics_store/items.csv')
        assert product.product_all[4].count_product == 5.5

    def test_check_int_count_is_int(self):
        """Проверка корректной работы метода is_integer для количества продукта
            при создании продукта из файла (целое число с дробной частью)"""

        Product.create_product_by_file('electronics_store/items.csv')
        assert product.product_all[3].count_product == 3

    def test_check_int_with_factorial_count_is_int(self):
        """Проверка корректной работы метода is_integer для цены продукта
            при создании продукта из файла (целое число)"""

        Product.create_product_by_file('electronics_store/items.csv')
        assert product.product_all[6].count_product == 5

    def test_check_repr_like_magic_methods(self):
        """Проверка корректной работы метода __repr__"""

        product_3 = Product('Смартфон', 10000, 20)
        assert product_3.__repr__() == "Product('Смартфон', 10000, 20)"

    def test_check_str_like_magic_methods(self):
        """Проверка корректной работы метода __str__ для класса Phone"""

        product_3 = Product('Смартфон', 10000, 20)
        assert product_3.__str__() == "Смартфон"

    def test_check_repr_like_user_func(self):
        """Проверка корректной работы метода __repr__"""

        product_3 = Product('Смартфон', 10000, 20)
        assert repr(product_3) == "Product('Смартфон', 10000, 20)"

    def test_check_str_like_user_func(self):
        """Проверка корректной работы метода __repr__"""

        product_3 = Product('Смартфон', 10000, 20)
        assert str(product_3) == "Смартфон"

    def test_setting_name_setter(self):
        """Проверка установки нового значения наименования продукта (name_product)
        через сеттер"""

        product_3 = Product('Смартфон', 10000, 20)
        product_3.name_product = "IPhone 12"
        assert str(product_3) == "IPhone 12"

    def test_add_product_and_product(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Product и Product"""

        product_3 = Product('Смартфон', 10000, 20)
        assert product + product_3 == 40

    def test_add_phone_and_num(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Product и числа"""
        product_3 = Product('Смартфон', 10000, 20)

        with pytest.raises(TypeError):
            (product_3 + 30)

    def test_add_phone_and_str(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Product и строки"""
        product_3 = Product('Смартфон', 10000, 20)

        with pytest.raises(TypeError):
            (product_3 + '30')
