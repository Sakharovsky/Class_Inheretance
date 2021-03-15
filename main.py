class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0

    def upd_avg(self):
        grade_list = []
        for grade_lists in self.grades.values():
            grade_list.extend(grade_lists)
        self.avg_grade = sum(grade_list) / len(grade_list)

    def __str__(self):
        self.upd_avg()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name} \n Фамилия: {self.surname} \nСредние оценки за домашние задания: {self.avg_grade} \nКурсы в процессе изучения: {courses_in_progress} \nЗавершенные курсы: {finished_courses}'

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        self.upd_avg()
        other.upd_avg()
        return self.avg_grade < other.avg_grade
    
    def __eq__(self, other):
        self.upd_avg()
        other.upd_avg()
        return self.avg_grade == other.avg_grade
    
    def __gt__(self, other):
        self.upd_avg()
        other.upd_avg()
        return self.avg_grade > other.avg_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.name = name
        self.surname = surname
        self.lecture_grades = {}
        self.avg_grade = 0
    
    def upd_avg(self):
        grade_list = []
        for grade_lists in self.lecture_grades.values():
            grade_list.extend(grade_lists)
        self.avg_grade = sum(grade_list) / len(grade_list)
    
    def __str__(self):
        self.upd_avg()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредние оценки за лекции: {self.avg_grade}'

    def __lt__(self, other):
        self.upd_avg()
        other.upd_avg()
        return self.avg_grade < other.avg_grade
    
    def __eq__(self, other):
        self.upd_avg()
        other.upd_avg()
        return self.avg_grade == other.avg_grade
    
    def __gt__(self, other):
        self.upd_avg()
        other.upd_avg()
        return self.avg_grade > other.avg_grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def avg_student_course(student_list, course):
    course_grades= []
    for student in student_list:
        if isinstance(student, Student) and course in student.grades:
            list_temp = student.grades.get(course)
            course_grades.extend(list_temp)
    if len(course_grades) != 0:
      return sum(course_grades) / len(course_grades)
    else:
      return 'Ошибка'

def avg_lecturer_course(lecturer_list, course):
    course_grades= []
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.lecture_grades:
            list_temp = lecturer.lecture_grades.get(course)
            course_grades.extend(list_temp)
    if len(course_grades) != 0:
      return sum(course_grades) / len(course_grades)
    else:
      return 'Ошибка'

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_in_progress += ['Python']

meh_student = Student('Fikus', 'Pikus', 'helicopter')
meh_student.courses_in_progress += ['JavaScript', 'Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
meh_reviewer = Reviewer('Another', 'Buddy')
meh_reviewer.courses_attached += ['JavaScript']

cool_lecturer = Lecturer('Another', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'JavaScript']

meh_lecturer = Lecturer('The other', 'Buddy')
meh_lecturer.courses_attached += ['JavaScript']

cool_reviewer.rate_hw(cool_student, 'Python', 10)
cool_reviewer.rate_hw(cool_student, 'Python', 10)
cool_reviewer.rate_hw(cool_student, 'Python', 10)
cool_reviewer.rate_hw(meh_student, 'Python', 7)

meh_reviewer.rate_hw(meh_student, 'JavaScript', 7)
meh_reviewer.rate_hw(meh_student, 'JavaScript', 7)
meh_reviewer.rate_hw(meh_student, 'JavaScript', 7)

cool_student.rate_lecture(cool_lecturer, 'Python', 9.9)
cool_student.rate_lecture(cool_lecturer, 'Python', 9.9)
cool_student.rate_lecture(cool_lecturer, 'Python', 9.9)

meh_student.rate_lecture(meh_lecturer, 'JavaScript', 9.9)
meh_student.rate_lecture(meh_lecturer, 'JavaScript', 9.9)
meh_student.rate_lecture(meh_lecturer, 'JavaScript', 9.9)
meh_student.rate_lecture(cool_lecturer, 'JavaScript', 10)

print(cool_lecturer.lecture_grades)
print(meh_student.grades)
print(meh_lecturer)
print(cool_student)
print(cool_lecturer > meh_lecturer)
print(meh_student == cool_student)

student_list = [cool_student, meh_student]
course = 'Python'
print(avg_student_course(student_list, course))

lecturer_list = [cool_lecturer, meh_lecturer]
course = 'JavaScript'
print(avg_lecturer_course(lecturer_list, course))