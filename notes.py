# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    # function that start with __ are not intended to be called directly
    def __init__(self, fc = "", a = 0, w = 0.0, n = "") -> None:
        """Create an instance of the dog class and
        set attributes"""
        self.fur_color = fc
        self.age = a
        self. weight = w
        self. name = n
        self.fetch_count = 0

    def __str__(self) -> str:
        s = "Dog's name is " + self.name + "\n"
        s += "and their age is " + str(self.age) + "\n"
        s += "and their fur color is " + self.fur_color + "\n"
        return s

    def play_fetch(self, num_times):
        self.fetch_count += num_times

bergdog = Dog("black", 7, 78.2, "logan")
ninadog = Dog("brown", 3, 100, "hobbes")

print(bergdog)
print(ninadog)

bergdog.play_fetch(20)
ninadog.play_fetch(15)

print(f"{ninadog.name} has played fetch {ninadog.fetch_count} times")