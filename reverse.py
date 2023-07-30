def reverse_string(temp):
    words = temp.split(" ")
    words = words[-1::-1]
    output = ' '.join(words)
    return output


if __name__ == "__main__":

    string = input("please input a string and i will reverse it\n")
    result = reverse_string(string)
    print(result)
