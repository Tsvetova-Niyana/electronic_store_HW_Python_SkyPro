from electronics_store.product import Product
from electronics_store.mixin_change_language import MixinChangeLanguage


class Keyboard(Product, MixinChangeLanguage):

    def __repr__(self) -> str:
        return f'Keyboard ({self.name_product}, {self.amount_product}, {self.count_product})'
