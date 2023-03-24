from electronics_store.phone import Phone
from electronics_store.product import Product

if __name__ == '__main__':
    product_1 = Product("Смартфон", 10000, 20)
    product_2 = Product("Ноутбук", 20000, 5)

    # Позитивная проверка инициализации экземпляра класса Phone
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 12", 100_000, 15, 2)



