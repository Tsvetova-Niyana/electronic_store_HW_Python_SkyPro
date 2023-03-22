"""
Создайте класс Phone. У этого товара есть все атрибуты класса Item
и еще атрибут для хранения количества сим-карт,  которые телефон поддерживает.
"""
from product import Product


class Phone(Product):
    def __init__(self, name_product, amount_product, count_product, number_supported_sim_cards):
        super().__init__(name_product, amount_product, count_product)
        self.__number_supported_sim_cards = number_supported_sim_cards

    @property
    def number_supported_sim_cards(self):
        return self.__number_supported_sim_cards

    @number_supported_sim_cards.setter
    def number_supported_sim_cards(self, value: int) -> None:
        if value <= 0 or not isinstance(value, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.number_supported_sim_cards = value