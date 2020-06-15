if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)

    new_arr = sorted(unique_arr, reverse = True)
    print(new_arr[1])