from product import Product

if __name__ == '__main__':
    product_1 = Product("Смартфон", 10000, 20)
    product_2 = Product("Ноутбук", 20000, 5)
    # product_2.name_product = "СуперНоутбук"

    print("\nПродукты:\n")
    print("Название товара: ", product_1.name_product)
    print("Цена товара: ", product_1.amount_product)
    print("Количество товара: ", product_1.count_product)
    print("Итоговая сумма: ", product_1.calculate_total_price())
    print()

    print("Название товара: ", product_2.name_product)
    print("Цена товара: ", product_2.amount_product)
    print("Количество товара: ", product_2.count_product)
    print("Итоговая сумма: ", product_2.calculate_total_price(), "\n")

    Product.pay_rate = 0.8
    product_1.apply_discount()
    print("Название товара: ", product_1.name_product)
    print("Цена товара: ", product_1.amount_product, "\n")

    print("Название товара: ", product_2.name_product)
    print("Цена товара: ", product_2.amount_product)

    print()
    print(Product.product_all)

    Product.create_product_by_file('items.csv')

    print(Product.product_all)

    for item in Product.product_all:
        print(item.name_product, item.amount_product, item.count_product)

    print(Product.is_integer(5))
    print(Product.is_integer(5.0))
    print(Product.is_integer(5.5))

    print()

    print(repr(product_1))
    print(product_1)
