import sys
import getopt

name = "default"
size = 100

opts, args = getopt.getopt(sys.argv[1:], "n:s:", ["name", "size"])

for opt, arg in opts:
    if opt in ("-n", "--name"):
        name = arg
    elif opt in ("-s", "--size"):
        size = int(arg)

for arg in args:
    print(f"Additional argument: {arg} ")

print(f"Name: {name}, Size: {size}")
print(f"script name: {sys.argv[0]}")
