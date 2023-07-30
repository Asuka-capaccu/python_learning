# 函数的定义
def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def demo(name, age):
    print("my name is {}, and my age is {}".format(name, age))


def test(name, age=30):
    print("my age is {}, and my name is {}".format(age, name))


def test02(age, *names):
    print("my age is %d" % age)
    print("my names are listed bellow")
    for name in names:
        print(name)


def test03(age, **names):
    print("my age is %d" % age)
    print("my names are listed bellow")
    for key, value in names.items():
        print("{} {}".format(key, value))


def test04(a, b, /, c, d, *, e, f):
    print("hello")


if __name__ == '__main__':
    # 函数的调用
    my_max(100, 109900)

    # 函数的参数传递机制 py可传可变对象和不可变对象 不区分值传递还是引用传递,其实适合java一样的传递方式

    # 必需参数 参数要以正确的顺序传入
    my_max(100, 109900)

    # 关键字参数 通过指定的方式传入参数,可以不按顺序
    demo(age=19, name='hello')

    # 默认参数
    test(name="hi")

    # 不定长参数 以元组的方式传入, 如果没有这个参数就是一个空元组
    test02(19, ("hello", "hi"))

    print("-------------------")
    test03(19, a=1, b=2, c=3)

    # lambda表达式 map返回值是迭代器而不是列表
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print(squares)

    # 强制位置参数
    # / 和 *, /现在很少用了
    # *后面的参数必须用关键字传输, /之前的参数是定位参数, 后面的参数是关键字参数
    test04(10, 20, 30, 40, e=50, f=60)
