from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


# === Product interface ===
class Vehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        """Perform the vehicle-specific action and return a message."""
        pass


# === Concrete products ===
class Car(Vehicle):
    def __init__(self, seats: int = 4):
        self.seats = seats

    def drive(self) -> str:
        return f"Car is driving with {self.seats} seats."


class Bike(Vehicle):
    def __init__(self, has_gears: bool = True):
        self.has_gears = has_gears

    def drive(self) -> str:
        gears = "with gears" if self.has_gears else "without gears"
        return f"Bike is riding {gears}."


class Truck(Vehicle):
    def __init__(self, capacity_tons: float = 5.0):
        self.capacity_tons = capacity_tons

    def drive(self) -> str:
        return f"Truck is hauling {self.capacity_tons} tons."


# === Factory ===
class VehicleFactory:
    """
    Simple Factory Method implementation.
    Register creators into the factory so adding new vehicle types
    does not require changing client code.
    """

    def __init__(self):
        self._creators: Dict[str, callable] = {}

    def register(self, key: str, creator: callable) -> None:
        """Register a creator callable under a key (e.g., 'car')."""
        self._creators[key.lower()] = creator

    def create(self, key: str, **kwargs) -> Vehicle:
        """Create a Vehicle instance corresponding to `key`."""
        try:
            creator = self._creators[key.lower()]
        except KeyError:
            raise ValueError(f"Vehicle type '{key}' is not registered.") from None
        product = creator(**kwargs)
        if not isinstance(product, Vehicle):
            raise TypeError("Creator did not return a Vehicle instance.")
        return product


# === Client code / usage ===
def main():
    factory = VehicleFactory()

    # Register concrete product constructors
    factory.register("car", lambda **kwargs: Car(**kwargs))
    factory.register("bike", lambda **kwargs: Bike(**kwargs))
    factory.register("truck", lambda **kwargs: Truck(**kwargs))

    # Create vehicles without knowing their concrete classes
    v1 = factory.create("car", seats=5)
    v2 = factory.create("bike", has_gears=False)
    v3 = factory.create("truck", capacity_tons=12.5)

    print(v1.drive())  # Car is driving with 5 seats.
    print(v2.drive())  # Bike is riding without gears.
    print(v3.drive())  # Truck is hauling 12.5 tons.


if __name__ == "__main__":
    main()
