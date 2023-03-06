class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.average_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def average_grade(self):
        all_grades = []
        for value in self.grades.values():
            all_grades.extend(value)
        return sum(all_grades) / len(all_grades)

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Несравнимо')
            return
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grade()}\n' \
              f'Ведёт курсы: {", ".join(self.courses_attached)}\n'
        return res

    def average_grade(self):
        all_grades = []
        for value in self.grades.values():
            all_grades.extend(value)
        return sum(all_grades) / len(all_grades)

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Несравнимо')
            return
        return self.average_grade() > other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

stud = Student('Бакс', 'Банни', 'Кролик')
stud.courses_in_progress += ['Git', 'Python']
stud.finished_courses.append('Введение')

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

rev = Reviewer('Kurt', 'Cobain')
rev.courses_attached += ['Python', 'Git']

test_testov = Lecturer('Test', 'Tesstov')
test_testov.courses_attached += ['Python', 'Git']

lect = Lecturer('Степа', 'Дядя')
lect.courses_attached += ['Python', 'Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(stud, 'Git', 8)
cool_mentor.rate_hw(stud, 'Git', 8)
cool_mentor.rate_hw(stud, 'Python', 9)
cool_mentor.rate_hw(stud, 'Python', 9)

stud.rate_lec(test_testov, 'Git', 10)
stud.rate_lec(test_testov, 'Git', 8)
stud.rate_lec(test_testov, 'Git', 8)
best_student.rate_lec(test_testov, 'Python', 10)
stud.rate_lec(test_testov, 'Введение', 7)

stud.rate_lec(lect, 'Git', 8)
best_student.rate_lec(lect, 'Python', 10)
best_student.rate_lec(lect, 'Python', 9)
best_student.rate_lec(lect, 'Git', 9)

students = [best_student, stud]
lecturers = [test_testov, lect]

# Реализовал одну функцию для подсчета средней оценки тк она работает и для студентов и для преподавателей.
def average_grade(students, cours):
    all_grades_course = []
    for st in students:
        for course, grade in st.grades.items():
            if course == cours:
                all_grades_course.extend(grade)
    avg_grade_in_course = sum(all_grades_course) / len(all_grades_course)
    return f'Средняя оценка на курсе {cours}: {avg_grade_in_course}'


print(test_testov < lect)
print(best_student > stud)
print(test_testov.average_grade())
print(test_testov.grades)
print(lect.grades)
print(best_student.grades)
print(stud.grades)
print(test_testov)
print(lect)
print(stud)
print(best_student)
print(cool_mentor)
print(average_grade(students, 'Python'))
print(average_grade(lecturers, 'Git'))

