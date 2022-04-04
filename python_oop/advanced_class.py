# example with more than one class
def main():
    class Student:
        def __init__(self, name, age, grade):
            self.name = name
            self.age = age
            self.grade = grade # 0 - 100

        def get_grade(self):
            return self.grade

    class Course:
        def __init__(self, name, max_students):
            self.name = name
            self.max_students = max_students
            self.students = []

        def add_student(self, student):
            if len(self.students) < self.max_students:
                self.students.append(student)
                print("add success")
                return True
            else: 
                print("exceeds max limit")
                return False
                

        def get_average_grade(self):
            value = 0
            for student in self.students:
                value += student.get_grade()

            return value / len(self.students)

    # declaration of Student class
    s1 = Student("Tim", 19, 95)
    s2 = Student("Bill", 19, 75)
    s3 = Student("Jill", 19, 65)

    # declaaration of Course class
    course = Course("Science", 2)
    course.add_student(s1)
    course.add_student(s2)
    # course.add_student(s3)

    # this returns raw output showing where the object value is located
    print(course.students)

    # calls both classes - indexes to the first student in the list
    print(course.students[0].name)

    print(course.get_average_grade())

if __name__ == '__main__':
    main()