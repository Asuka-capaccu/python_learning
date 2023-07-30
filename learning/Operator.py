if __name__ == '__main__':

    # =是没有返回值的 :=是有返回值的

    a = "hellooooooooooooo"
    # 海象运算符的两种运用方式
    if (n := len(a)) > 10:
        print(f"List is too long ({n} elements, expected <= 10)")
        print("{n}".format(n=n))

    # and not or
    print(0 and 100)

    # 元素是否在序列中 in / not in
    string1 = "hello"
    print('h' in string1)

    # 判断两个表示符是否引用一个对象 is / is not
    string2 = string1
    print(string1 is string2)
