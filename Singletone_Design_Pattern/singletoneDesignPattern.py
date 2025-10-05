from abc import ABC, abstractmethod

class IPerson(ABC):

    @abstractmethod
    def print_data(self):
        pass

class Person(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if Person.__instance is None:
            Person.__instance = Person("Default Name", 0)  # Default values
        return Person.__instance

    def __init__(self, name, age):
        if Person.__instance is None:  # Prevent re-initialization
            self.name = name
            self.age = age
            Person.__instance = self
        else:
            raise Exception("This class is a singleton! Use get_instance() method.")

    def print_data(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("John", 30)
p1.print_data()
p2 = Person.get_instance()
p2.print_data()