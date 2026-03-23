import logging
from people import Customer
from products import Product
from utilities import is_adult


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
            v: str = input("Do you have parental permission? y/n: ").lower().strip()

            if not is_adult(v):
                logging.error("the user is a minor, program closed ❌")

                raise ValueError("You need parental permission")

        if customer.product is None:
            logging.error("The customer has not added any products ❌")

            raise ValueError("Customer has no product assigned")

        logging.info("Withdraw validation was successful ✅")

        return customer.product.rent()

    def return_(self, customer: Customer, product: Product):
        if customer.product is None:
            logging.error("The customer did not rent any products ❌")

            raise ValueError("Customer has no product assigned")

        logging.info("return function validation was successful ✅")

        return customer.product.return_()
