"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(product.quantity - 1)
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity + 1)

    def test_product_buy(self, product):
        product.buy(10)
        assert product.quantity == 990


    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError) as exc_info:
            product.buy(product.quantity + 1)
        assert exc_info.type is ValueError
        assert exc_info.value.args[0] == "Данного товара нет в наличии"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        cart.add_product(product, 2)

        assert cart.products[product] == 2

    def test_remove_product(self, cart, product):
        cart.clear()
        cart.add_product(product, 2)
        cart.remove_product(product)


        assert cart.products == {}


        cart.clear()
        cart.add_product(product, 2)
        cart.remove_product(product, 5)

        assert cart.products == {}


        cart.add_product(product, 2)
        cart.remove_product(product, 1)

        assert cart.products[product] == 1

    def test_clear(self, cart):
        cart.clear()

        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product,  1)
        assert cart.products[product] == 1
        assert cart.get_total_price() == 100.0



    def test_buy(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()

        assert cart.products == {}







