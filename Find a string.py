def count_substring(string, sub_string):
    length_string = len(string)
    length_substring = len(sub_string)
    count = 0
    for i in range(0,length_string):
        if (string[i:i+length_substring]==sub_string):
            count+=1
            #return i
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)