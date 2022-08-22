class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                Lecturer.grades[course] += [grade]
            else:
                Lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def Average_Student(self, grades, lang):
        res = round(sum(self.grades[lang]) / len(self.grades[lang]), 1)
        return res
    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_grade}\n Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n Завершенные курсы: {" ".join(self.finished_courses)}'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.speeking_courses = []
        self.courses_attached = []
    grades = {}
    def Average_Lecturer(grades, lang):
        res = round(sum(grades[lang]) / len(grades[lang]), 1)
        return res
    def __str__(self):
        return f'Имя: {self.name }\n Фамилия: {self.surname}\n Средняя оценка за лекции: {Average_Lecturer(self.grades, "Python")}'
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}'

def Average_Lecturer(grades, lang):
    res = round(sum(grades[lang]) / len(grades[lang]), 1)
    return res
def comparison_of_grades(Student_grades, Lecturer_grades):
    if Student_grades > Lecturer_grades:
        print("Средняя оценка студента выше чем у лектора")
    else:
        print("Средняя оценка луктора выше чем устудента")
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.average_grade = best_student.Average_Student(best_student.grades, "Python")
cool_Lecturer = Lecturer('Nikita', 'Chebotarev')
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python'] 
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
best_student.rate_Lecturer(cool_Lecturer, 'Python', 10)
best_student.rate_Lecturer(cool_Lecturer, 'Python', 9)
best_student.rate_Lecturer(cool_Lecturer, 'Python', 10)
#print(cool_Lecturer.grades)
print(best_student.grades)
#print(cool_reviewer)
#print(cool_Lecturer)
print(best_student)