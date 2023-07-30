from builtins import print

if __name__ == '__main__':
    # 基本操作
    str1 = 'hello'
    print(str1[0])
    print(str1[-1])
    print(str1[0:-1])
    print(str1 * 2)
    print(str1 + " world")

    # 格式化请看format.py

    # unicode
    str2 = u"你好啊"
    print('\u22ff'.isalpha())

    # 常见的API 演示split和join的用法
    # https://www.runoob.com/python3/python3-string.html
    str3 = "My love is like a red red rose"
    ll = str3.split(' ')
    ll = ll[-1::-1]
    print(ll)
    str4 = '-'.join(ll)
    print(str4)
