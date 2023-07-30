if __name__ == '__main__':
    print("hello world")
    name = input()
    age = int(input())
    # 类似c语言的格式化
    print("My name is %s, and my age is %d" % (name, age))

    # String format
    print("My name is {}, and my age is {}".format(name, age))
    print("My name is {0}, and my age is {1}".format(name, age))
    print("My name is {n}, and my age is {a}".format(n=name, a=age))

    # f-string
    print(f"My name is {name}, and my age is {age}")

    # 关于format更多的格式细节，用到再查询
