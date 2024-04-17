if __name__ == '__main__':
    students=[]
    SecondLowest=[]
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)

    second=sorted(list(set(scores)))[1]

    for student in students:
        if student[1]==second:
            SecondLowest.append(student[0])
    
    for S in sorted(SecondLowest):
        print(S)
