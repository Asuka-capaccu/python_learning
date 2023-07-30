
if __name__ == '__main__':
    ll = ['my', 'love', 'is', 'like', 'a', 'red', 'red', 'rose']
    it = iter(ll)
    for x in it:
        print(x)

    while True:
        try:
            print(next(it))
        except StopIteration:
            pass

    # 异常用于标识迭代的完成，防止出现无限循环的情况
    
