def reverseWords(astr):
    inputWords = astr.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


if __name__ == '__main__':
    ll = ['hello', 123, True, False]
    print(ll)
    print(ll[0])
    print(ll[1:3])
    print(ll + ['world'])
    print(ll * 2)

    # 设置步长
    print(ll[0::2])

    # 从后往前截取
    print((ll[-1::-1]))

    print(reverseWords("hello world hahaha"))

    ll.append("rose")

    del ll[2]

    print(123 in ll)

    # https://www.runoob.com/python3/python3-list.html



