def swap_case(s):

    l = list(s)
    temp_list = []

    for i in l:
        j = ""
        if i.islower():
            j = i.upper()
        elif i.isupper():
            j = i.lower()
        else:
            temp_list.append(i)
        temp_list.append(j)

    result = ''.join(temp_list)
    
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)