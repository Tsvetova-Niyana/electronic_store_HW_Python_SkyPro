from electronics_store.phone import Phone, Product
import pytest


class TestTelephones:
    def test_init(self):
        """Проверка инициализации экземпляра класса Phone"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1 is not None

    def test_name(self):
        """Проверка корректного получения наименования продукта (name_product)"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1.name_product == "iPhone 14"

    def test_amount_product(self):
        """Проверка корректного получения цены продукта (amount_product)"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1.amount_product == 120_000

    def test_count_product(self):
        """Проверка корректного получения количества продукта (count_product)"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1.count_product == 5

    def test_number_supported_sim_cards(self):
        """Проверка корректного получения количества поддерживаемых сим-карт (number_supported_sim_cards)"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1.number_supported_sim_cards == 2

    def test_change_number_supported_sim_cards(self):
        """Проверка установки нового значения количества поддерживаемых сим-карт (number_supported_sim_cards)
        через сеттер"""
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        phone1.number_supported_sim_cards = 1
        assert phone1.number_supported_sim_cards == 1

    def test_pay_rate(self):
        """Проверка корректного получения уровня скидки (pay_rate)"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        Product.pay_rate = 1.1
        assert phone1.pay_rate == 1.1

    def test_product_all(self):
        """Проверка корректного получения перечня всех продуктов (product_all)"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert phone1.product_all == Product.product_all

    def test_change_number_supported_sim_card_by_zero(self):
        """Проверка установки нового значения количества поддерживаемых сим-карт (number_supported_sim_cards) = 0"""
        phone1 = Phone("iPhone 14", 120_000, 5, 2)

        with pytest.raises(ValueError):
            phone1.number_supported_sim_cards = 0

    def test_change_number_supported_sim_card_by_less_zero(self):
        """Проверка установки нового значения количества поддерживаемых сим-карт (number_supported_sim_cards) =
        отрицательному значению"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)

        with pytest.raises(ValueError):
            phone1.number_supported_sim_cards = -2

    def test_change_number_supported_sim_card_by_factorial(self):
        """Проверка установки нового значения количества поддерживаемых сим-карт (number_supported_sim_cards) =
           дробному значению"""

        phone1 = Phone("iPhone 14", 120_000, 5, 2)

        with pytest.raises(ValueError):
            phone1.number_supported_sim_cards = 2.5

    def test_change_number_supported_sim_card_by_str(self):
        """Проверка установки нового значения количества поддерживаемых сим-карт (number_supported_sim_cards) =
          строковому значению"""
        phone1 = Phone("iPhone 14", 120_000, 5, 2)

        with pytest.raises(TypeError):
            phone1.number_supported_sim_cards = '2'

    def test_repr(self):
        """Проверка корректной работы метода __repr__(переопределен для класса Phone)"""
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert repr(phone1) == "Phone('iPhone 14', 120000, 5)"

    def test_str(self):
        """Проверка корректной работы метода __str__ для класса Phone"""
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert str(phone1) == "iPhone 14"

    def test_add_phone_and_phone(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Phone и Phone"""
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        phone2 = Phone("iPhone 12", 100_000, 15, 2)
        assert phone1 + phone2 == 20

    def test_add_phone_and_product(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Phone и Product"""
        phone1 = Phone("iPhone 14", 120_000, 15, 2)
        product = Product("iPhone 12", 100_000, 15)
        assert phone1 + product == 30

    def test_add_phone_and_num(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Phone и числа"""
        phone1 = Phone("iPhone 14", 120_000, 15, 2)

        with pytest.raises(TypeError):
            (phone1 + 30)

    def test_add_phone_and_str(self):
        """Проверка корректной работы метода __add__ для сложения экземпляров класса Phone и строки"""
        phone1 = Phone("iPhone 14", 120_000, 15, 2)

        with pytest.raises(TypeError):
            (phone1 + '30')
