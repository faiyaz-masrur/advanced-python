from abc import ABC, abstractmethod

# Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass


# Real Subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")


# Proxy (like middlewear)
class ProxyImage(Image):
    def __init__(self, filename):
        # Add extra functionality (checking, logging)
        self.filename = filename
        self.real_image = None  # Lazy initialization

    def display(self):
        # Load the real image only when needed
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        # Add extra functionality (checking, logging)
        self.real_image.display()


# Client code
if __name__ == "__main__":
    image1 = ProxyImage("photo1.png")
    image2 = ProxyImage("photo2.png")


    print("First call:")
    image1.display()  # Loads + displays

    print("\nSecond call:")
    image1.display()  # Just displays (already loaded)

    print("\nDifferent image:")
    image2.display()  # Loads + displays
