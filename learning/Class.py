class People:

    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):

        return f"My name is {self.name}, I am {self.age} years old.\n{self.gender} and {self.address}"


if __name__ == '__main__':
    x = People("hello", 10, "male", "shanghai")
    print(x)
