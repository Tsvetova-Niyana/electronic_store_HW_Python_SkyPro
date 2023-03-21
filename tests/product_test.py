import csv
import os

from electronics_store.product import Product
import pytest

product = Product("Смартфон", 10000, 20)


class TestProduct:
    def test_check_name_at_init_product(self):
        assert product.name_product == "Смартфон"

    def test_check_amount_product_at_init_product(self):
        assert product.amount_product == 10000

    def test_check_count_product_at_init_product(self):
        assert product.count_product == 20

    def test_check_pay_rate_at_init_product(self):
        assert product.pay_rate == 1

    def test_check_product_all_at_init_product(self):
        product_2 = Product("Ноутбук", 20000, 5)
        assert product.product_all == [product, product_2]

    def test_calculate_total_price(self):
        assert product.calculate_total_price() == 200_000

    def test_change_pay_rate(self):
        Product.pay_rate = 0.85
        assert product.pay_rate == 0.85

    def test_apply_discount(self):
        product.apply_discount()
        assert product.amount_product == 8_500

    def test_type_name(self):
        assert type(product.name_product) == str

    def test_type_amount_product(self):
        assert type(product.amount_product) == float

    def test_type_count_product(self):
        assert type(product.count_product) == int

    def test_type_pay_rate(self):
        assert type(product.pay_rate) == float

    def test_type_product_all(self):
        assert type(product.product_all) == list

    def test_init_exeptions(self):
        with pytest.raises(TypeError):
            Product()

    def test_check_len_name_exeptions(self):
        with pytest.raises(ValueError):
            product.name_product = "СуперНоутбук"

    def test_open_file(self):
        current = os.getcwd()
        folder = "electronics_store"
        full_path = os.path.join(current, folder, "items.csv")

        with open(full_path) as file:
            result = csv.DictReader(file)
        assert result is not None

    def test_create_product_by_file(self):
        Product.create_product_by_file('electronics_store/items.csv')
        assert len(product.product_all) == 7
