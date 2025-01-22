# Ms.LaRose and Vienna creating a thing
import random

def rand_num():
    num = random.randint(1,100)
    return num

def helloWorld(name):
    return f"Hello {name}!"


def main():
    print("Welcome to my program, please type your name: \n")
    name = input()
    print(helloWorld(name))
    print(rand_num())


main()