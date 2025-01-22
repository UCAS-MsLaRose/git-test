# Ms.LaRose and Vienna creating a thing

def helloWorld(name):
    return f"Hello {name}!"


def main():
    print("Welcome to my program, please type your name: \n")
    name = input()
    print(helloWorld(name))
    print(f"{name} this program lets you get a random number\nenter 1 to get a random number\nenter 2 to see your last number\n")
    choice = input()

main()