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
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за домашние задания: {Average(self.grades, "Python")}')
        print(f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}')
        return f'Завершенные курсы: {" ".join(self.finished_courses)}'
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
    def __str__(self):
        print(f'Имя: {self.name }')
        print(f'Фамилия: {self.surname}')
        return f'Средняя оценка за лекции: {Average(self.grades, "Python")}'
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
        print(f'Имя: {self.name}')
        return f'Фамилия: {self.surname}'
def Average(grades, lang):
    res = round(sum(grades[lang]) / len(grades[lang]), 1)
    return res
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
cool_Lecturer = Lecturer('Nikita', 'Chebotarev')
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python'] 
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
best_student.rate_Lecturer(cool_Lecturer, 'Python', 10)
best_student.rate_Lecturer(cool_Lecturer, 'Python', 9)
best_student.rate_Lecturer(cool_Lecturer, 'Python', 10)
print(cool_Lecturer.grades)
print(best_student.grades)
print(cool_reviewer)
print(cool_Lecturer)
print(best_student)