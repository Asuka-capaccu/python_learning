from builtins import print

if __name__ == '__main__':
    # Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
    s1 = {"hello", 100, True, 11231.313}
    # 将集合中的元素逐个加入到set中
    s2 = set("world")
    print(s1)
    print(s2)
    s1.add("world")
    s1.update("ha", "he")

    # delete 如果元素不存在,一个会发生错误,另一个不会 随即删除
    s1.remove("he")
    s1.discard("he")
    s1.pop()

    # 创建一个空集合
    s2 = set()
    # s3 = {} 错误的做法

    # 集合的运算
    ss = {"hello", "world", "false", "true", "going"}
    sss = {"hi", "word", "false", "true", "goto"}
    print(ss - sss)
    print(ss | sss)
    print(ss & sss)
    print(ss ^ sss)

    # https://www.runoob.com/python3/python3-set.html
