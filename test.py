from enum import  Enum


class Fruit(Enum):
    apple = "Apple"
    mango = "Mango"
    orange = "Orange"


print("Testing")
print(Fruit.apple)
print(Fruit.mango)

apple = Fruit.apple
mango = Fruit.mango