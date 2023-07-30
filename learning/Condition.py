if __name__ == '__main__':
    a = 100
    b = 10000
    c = 12000
    if a > b:
        print("hello")
    elif b < c:
        print("haha")
    else:
        print("dedede")

    num = input()

    match int(num):
        case 400:
            print("bad request")
        case 404:
            print("not found")
        case _:
            print("hello")
