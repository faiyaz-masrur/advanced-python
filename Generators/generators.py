import sys

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

values = infinite_counter()

for _ in range(5):
    print(next(values))

print(f"generator size: {sys.getsizeof(values)} bytes")

