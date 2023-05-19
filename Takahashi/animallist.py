import sys
args = sys.argv

animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal.insert(int(args[1]), args[2])
del animal[-1]
animal.sort()
print(animal,end="")
