"""Rental company project"""

import os
import logging
from dotenv import load_dotenv
from people import Employed, Customer
from products import Movie, TvShow
from rental_shop import RentalShop


logging.basicConfig(level=logging.DEBUG)
load_dotenv()

shop_name = os.getenv("SHOP_NAME")

cashier = Employed(name="John Kennedy", age=32, badge=3232)

lion_king = Movie(name="Lion King", price=25.90, expiration=7, duration=120, rating="G")
narcos = TvShow(name="Narcos", price=39.90, expiration=27, rating="R", seasons=3)

neymar = Customer(name="Neymar jr", age=32, registration_number=1017)
john = Customer(name="john xv", age=13, registration_number=1027)

neymar.product = narcos
john.product = lion_king

lb = RentalShop(name=shop_name)
lb.customers.append(neymar)
lb.customers.append(john)

lb.employees.append(cashier)

lb.products.append(narcos)
lb.products.append(lion_king)

print(lb.rent(neymar, narcos))
# print(lb.return_(neymar, narcos))

print(lb.rent(john, lion_king))
# print(lb.return_(john, lion_king))
