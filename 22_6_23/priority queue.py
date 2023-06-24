students_grade=[]
org=[]
students_grade.append((1,"Akash"))
students_grade.append((4,"Ankitha"))
students_grade.append((2,"yash"))
students_grade.append((5,"arun"))
students_grade.append((3,"babu"))
org=students_grade
students_grade.sort(reverse=True)
print(f"priority wise:{students_grade}")
print("original queue:")
while org:
    print(org.pop())

