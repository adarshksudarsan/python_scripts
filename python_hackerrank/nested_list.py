'''
Given the names and grades for each student in a class of students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
print("marksheet",marksheet)
second_highest = sorted(list(set([marks for name, marks in marksheet])))[-2]
print(sorted(list(set([marks for name, marks in marksheet]))))
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))