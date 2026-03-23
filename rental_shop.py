import logging
from people import Customer
from products import Product
from utilities import has_permission


class RentalShop:
    """Here is the main system that connects all the other classes"""

    def __init__(self, name: str | None) -> None:
        self.name = name
        self.customers = []
        self.employees = []
        self.products = []

    def rent(self, customer: Customer, product: Product):
        if product not in self.products:
            logging.error("Product not found in the shop's product list ❌")

            raise ValueError("Unknown Product")

        if customer.age < 18 and product.rating == "R":
            if not has_permission():
                logging.error("the user is a minor, program closed ❌")

                raise ValueError("You need parental permission")

        return product.rent()

    def return_(self, product: Product):
        return product.return_()
