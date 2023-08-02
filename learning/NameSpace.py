# build-in names
# global names
# local names

# local enclosing global build-in

# global nonlocal


num = 1


def func():
    global num
    num = 123
    print(num)
    print("hello")


func()
print(num)