# 在 python 用 import 或者 from...import 来导入相应的模块。
#
# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *

if __name__ == '__main__':
    num1 = 100
    num2 = 1000
    num3 = 100000
    num4 = num1 + \
           num2

    bool1 = True
    bool2 = False
    float1 = 1.23
    c1 = 1 + 2j
    str1 = 'hello'
    str2 = r'hello\n'
    print(str2)
    str3 = 'this ' 'is ' 'hello\n'
    str4 = 'this ' + 'is ' + 'hello\n'
    print(str3)
    print(str4)
    print(str3)
    print(str4)
    print(num1, end="")
    a, b, c = 1, 2, "runoob"
