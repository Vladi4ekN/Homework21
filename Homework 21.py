class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                products = file.read().strip()
                return products
        except FileNotFoundError:
            return ''  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        existing_products = self.get_products().split('\n')
        existing_names = [line.split(', ')[0] for line in existing_products if line]

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in existing_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(str(product) + '\n')

potato = Product('Potato', 50.0, 'Vegetables')
apple = Product('Apple', 30.5, 'Fruits')
shop = Shop()
shop.add(potato, apple)
shop.add(potato)
print(shop.get_products())
