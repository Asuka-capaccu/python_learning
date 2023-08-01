print("this is reverse.py")


def reverse_string(temp):
    words = temp.split(" ")
    words = words[-1::-1]
    output = ' '.join(words)
    return output


def reverse_int(temp):
    temp_str = str(temp)
    temp_str = temp_str[-1::-1]
    return int(temp_str)


if __name__ == "__main__":
    string = input("please input a string and i will reverse it\n")
    result = reverse_string(string)
    print(result)
