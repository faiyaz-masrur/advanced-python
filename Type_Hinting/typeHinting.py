from typing import List, Optional

class User:
    def __init__(self, name: str, age: int, hobbies: Optional[List[str]] = None) -> None:
        self.name: str = name
        self.age: int = age
        self.hobbies: List[str] = hobbies if hobbies else []

    def add_hobby(self, hobby: str) -> None:
        self.hobbies.append(hobby)

    def get_profile(self) -> str:
        hobbies_text = ", ".join(self.hobbies) if self.hobbies else "no hobbies"
        return f"Name: {self.name}, Age: {self.age}, Hobbies: {hobbies_text}"


# Example usage
user1 = User("Faiyaz", 24, ["Singing", "Coding"])
user1.add_hobby("Reading")
print(user1.get_profile())