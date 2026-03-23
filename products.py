from abc import ABC, abstractmethod
from utilities import finalize_film_transaction, finalize_show_transaction
import logging


class Product(ABC):
    """abstract class for the rental company's products"""

    def __init__(self, name: str, price: float, expiration: int, rating: str) -> None:
        self.name = name
        self.price = price
        self.expiration = expiration
        self.rating = rating
        self.rented = False

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if new_rating not in ["G", "R"]:
            raise ValueError("Fill in only the indicative classifications available")

        self._rating = new_rating

    @abstractmethod
    def rent(self): ...

    def return_(self):
        logging.debug("Starting the return method..")

        if not self.rented:
            logging.error("The product was not rented ❌")

            raise ValueError("Product unavailable, the product was not rented")

        self.rented = False

        logging.info("Successful validation ✅")

        return f"The product {self.name} was returned"


class Movie(Product):
    """subclass responsible for registering films"""

    def __init__(
        self, name: str, price: float, expiration: int, rating: str, duration: int
    ) -> None:
        super().__init__(name, price, expiration, rating)

        self.duration = duration

    def rent(self):
        self.rented = True

        return finalize_film_transaction(self)


class TvShow(Product):
    """subclass responsible for registering Tv Shows"""

    def __init__(
        self, name: str, price: float, expiration: int, rating: str, seasons: int
    ) -> None:
        super().__init__(name, price, expiration, rating)

        self.seasons = seasons

    def rent(self):
        self.rented = True

        return finalize_show_transaction(self)
