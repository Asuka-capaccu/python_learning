import sys
from reverse import reverse_int, reverse_string

# import <name>
# from <name> import <name or *>

# 打印搜索模块的列表
print('\n', sys.path)

str1 = "hello world"
print(reverse_string(str1))

if __name__ == '__main__':
    # 仅在自身运行时执行, 被导入时不执行
    print("running")

    # 找到模块内定义的所有名称
    print(dir())
