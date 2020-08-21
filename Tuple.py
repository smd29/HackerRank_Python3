if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    new_list = []
    for i in integer_list:
        new_list.append(i)
    tup = tuple(new_list)

    h = hash(tup)
    print(h)
