# int float bool complex
if __name__ == '__main__':
    a = 1000
    print(type(a))
    print(isinstance(a, int))
    b = True
    print(isinstance(b, int))
    print(issubclass(bool, int))
    # print(True is 1)
    print(1 == True)
    print(10 // 3)
    print(2 ** 3)
    print(10 + 3j)
    print(complex(1, 3))
