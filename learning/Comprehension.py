if __name__ == '__main__':
    # [表达式 for 变量 in 列表]
    # [out_exp_res for out_exp in input_list]
    # [表达式 for 变量 in 列表 if 条件]
    # [out_exp_res for out_exp in input_list if condition]
    ll = [i ** 2 for i in range(1, 101) if i % 3 == 0]
    print(ll)

    # {key_expr: value_expr for value in collection}
    # {key_expr: value_expr for value in collection if condition}
    ll = [3, 4, "hello", 7, "world", 3.14]
    d = {x: i + 1 for i, x in enumerate(ll)}
    print(d)
    # 每次迭代返回一个包含两个元素的元组，分别表示当前元素的索引和值

    # 集合推导式和元组推导式是同样的写法

    
