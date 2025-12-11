count = int(input("Enter number of students:"))
marks = []

for i in range(count):
    student = {}
    student["name"] = input("Enter Student Name:")
    student["maths"] = int(input("Enter maths:"))
    student["science"] = int(input("Enter science:"))
    student["social"] = int(input("Enter social:"))
    marks.append(student)

total = lambda a,b,c: a+b+c

def avg(a,b,c):
    total = (a+b+c)//3
    return total
    
print("\n----- RESULTS -----")

for student in marks:
    a = student["maths"]
    b = student["science"]
    c = student["social"]

    print(student["name"])
    print("Average=",avg(a,b,c))
    print("Total=",total(a,b,c))


    if avg(a,b,c) >= 90:
        print("A Grade")
    elif avg(a,b,c) >= 80:
        print("B Grade")
    elif avg(a,b,c) >= 70:
        print("C Grade")
    elif avg(a,b,c) >= 60:
        print("D Grade")
    elif avg(a,b,c) >= 50:
        print("E Grade")
    else:
        print("Failed")