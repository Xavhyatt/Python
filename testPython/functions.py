students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    studenets_titlecase = get_students_titlecase()
    print(studenets_titlecase)


def add_student(name, student_id=100):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def new_student():
    q1 = input("Do you want to add a student?")
    if q1=="yes":
        student_name = input("Enter Student Name: ")
        student_id = input("Enter Student ID: ")

        add_student(student_name, student_id)
        save_file(student_name)
        new_student()


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


def read_students(f):
    for line in f:
        yield line

read_file()
print_students_titlecase()

new_student()
