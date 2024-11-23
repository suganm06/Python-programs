def find_students_with_maximum_score(scores):
    max_score = max(scores.values())
    max_score_students = [student for student, score in scores.items() if score == max_score]
    return sorted(max_score_students)

T = int(input())

for _ in range(T):
    N = int(input()) 
    scores = {} 

    for _ in range(N):
        student_name, score = input().split()
        scores[student_name] = float(score)

    max_score_students = find_students_with_maximum_score(scores)
    for student in max_score_students:
        print(student)
