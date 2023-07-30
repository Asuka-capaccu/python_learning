if __name__ == '__main__':
    # 创建的方式
    dic = {}
    dic["hello"] = 100
    dic["world"] = 101

    dic2 = {"hello": 100, "world": 101}

    del dic["hello"]

    # 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

    # 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

    # https://www.runoob.com/python3/python3-dictionary.html
