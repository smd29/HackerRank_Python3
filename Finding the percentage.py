if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    name_list = list(student_marks.keys())
    score_list = list(student_marks.values())

    #print(name_list)
    #print(score_list)

    query_name_index = name_list.index(query_name)
    

    avg_score = sum(score_list[query_name_index])/3

    print("{0:.2f}".format(avg_score))