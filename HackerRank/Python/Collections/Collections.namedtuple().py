import collections

n = int(input())
scol = ",".join(input().split())
Student = collections.namedtuple("Student", scol)

sum_ = 0 
for _ in range(n):
    row = input().split()
    student = Student(*row)
    sum_ += int(student.MARKS)

print(sum_ / n)
