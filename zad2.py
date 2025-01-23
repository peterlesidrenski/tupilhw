n = int(input())
students = {}
for _ in range(n):
    name_grade = tuple(input().split())
    name, grade = name_grade
    if name not in students.keys():
        students[name] = []
        students[name].append(float(grade))
for name, grades in students.items():
    avg = sum(grades)/len(grades)
    list_for_print = " ".join(f"{x:.2f}"for x in grades)
    print(f"{name} - {list_for_print}(avg: {avg:.2f})") 