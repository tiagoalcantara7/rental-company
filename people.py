from abc import ABC
from products import Product


class People(ABC):
    """
    Abstract class that supports subclasses
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


class Customer(People):
    """This subclass is responsible for registering customer data in the system"""

    def __init__(self, name: str, age: int, registration_number: int) -> None:
        super().__init__(name, age)
        self.registration_number = registration_number
        self.product: Product | None = None


class Employed(People):
    """This subclass is responsible for registering employee data"""

    def __init__(self, name: str, age: int, badge: int) -> None:
        super().__init__(name, age)
        self.badge = badge
