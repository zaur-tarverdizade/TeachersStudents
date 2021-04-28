LecturerList = []
StudentList = []

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = []
        self.grade = []
        StudentList.append(self)

    def print_best(self):
        for f in StudentList:
            print(f)

    def __lt__(self, other):
        if isinstance(other, Student):
            return sum(other.grade) / len(other.grade) < sum(self.grade) / len(self.grade)

    def rate_mntr(self, mentor, course, grade):
        if isinstance(mentor, lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
                mentor.grade.append(grade)
            else:
                mentor.grades[course] = [grade]
                mentor.grade.append(grade)
        else:
            print( 'Ошибка')

    def avrg_rd(self):
        for name_course, grade in self.grades.items():
            average_grade = sum(grade) / len(grade)
            self.avg_grade.append(name_course + " -> " + str(average_grade))

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname + "\nКурсы в процессе изучения: " + ",".join(self.courses_in_progress) + "\nЗавершенные курсы: " + ",".join(self.finished_courses) + "\nСредняя оценка за домашние задания: " + " , ".join(self.avg_grade)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.avg_grades = []
        self.bestlist = []



class lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.avg_grade = []
        self.grade = []
        LecturerList.append(self)


    def print_best(self):
        for f in LecturerList:
            print(f)


    def avrg_rd(self):
        for name_course, grade in self.grades.items():
            average_grade = sum(grade) / len(grade)
            self.avg_grade.append(name_course + " -> " + str(average_grade))

    def __lt__(self, other):
        if isinstance(other, lecturer):
            return sum(other.grade) / len(other.grade) < sum(self.grade) / len(self.grade)

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname + "\nСредняя оценка за лекции: " + " ".join(self.avg_grade)

class reviwer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.total_grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                self.total_grades[course] += [grade]
                student.grade.append(grade)
            elif course in self.total_grades:
                student.grades[course] = [grade]
                self.total_grades[course] += [grade]
                student.grade.append(grade)
            else:
                student.grades[course] = [grade]
                self.total_grades[course] = [grade]
                student.grade.append(grade)
        else:
            return 'Ошибка'

    def avg_ttl_grds(self, course):
        if course in self.total_grades:
            print("Средняя оценка за д/з по курсу "  + course + ": " + str(sum(self.total_grades.get(course))/len(self.total_grades.get(course)) ))

    # def avg_grade(self,student, course):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             average_grade = sum(student.grades[course])/len(student.grades[course])
    #             print(average_grade)
    #     else:
    #         print("Ошибка")

    # def comp(self, student1, student2, name_course):
    #     if isinstance(student1, Student) and isinstance(student2, Student) and name_course in self.courses_attached and name_course in student1.courses_in_progress and name_course in student2.courses_in_progress:
    #         if sum(student1.grades[name_course]) / len(student1.grades[name_course]) > sum(student2.grades[name_course]) / len(student2.grades[name_course]):
    #             print("Студент с большей оценкой по курсу " + name_course +  " : " + student1.name + ' ' + student1.surname)
    #
    #         elif sum(student1.grades[name_course]) / len(student1.grades[name_course]) < sum(student2.grades[name_course]) / len(student2.grades[name_course]):
    #             print("Студент с большей оценкой по курсу " + name_course +  " : " + student2.name + ' ' + student2.surname)

    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname

 
HPotter = Student('Harry', 'Potter')
HPotter.courses_in_progress += ['Python']
HPotter.courses_in_progress += ['Git']
HPotter.courses_in_progress += ['Java']
HPotter.courses_in_progress += ['MatLab']
HPotter.finished_courses += ["Введение в программирование"]

RWeasley = Student('Ronald', 'Weasley')
RWeasley.courses_in_progress += ['Python']
RWeasley.courses_in_progress += ['Java']
RWeasley.finished_courses += ["Введение в программирование"]
RWeasley.courses_in_progress += ['Git']
RWeasley.courses_in_progress += ['MatLab']

SSnape = reviwer('Severus', 'Snape')
SSnape.courses_attached += ['Python']
SSnape.courses_attached += ['Hub']

HSlughorn = reviwer('Horace' , 'Slughorn')
HSlughorn.courses_attached += ['Java']

MMcConnagal = lecturer('Minevra', 'McConnagal')
MMcConnagal.courses_attached += ['Git']

RLupin = lecturer('Remus', 'Lupin')
RLupin.courses_attached += ['MatLab']

# MMcConnagal = Mentor
# RLupin = Mentor


SSnape.rate_hw(HPotter, 'Python', 10)
SSnape.rate_hw(HPotter, 'Python', 7)
SSnape.rate_hw(HPotter, 'Python', 1)

SSnape.rate_hw(RWeasley, 'Python', 10)
SSnape.rate_hw(RWeasley, 'Python', 33)
SSnape.rate_hw(RWeasley, 'Python', 2)

HSlughorn.rate_hw(RWeasley, 'Java', 6)
HSlughorn.rate_hw(RWeasley, 'Java', 7)
HSlughorn.rate_hw(RWeasley, 'Java', 5)

HSlughorn.rate_hw(HPotter, 'Java', 1)
HSlughorn.rate_hw(HPotter, 'Java', 20)
HSlughorn.rate_hw(HPotter, 'Java', 6)

# SSnape.avg_grade(HPotter, 'Python')
# SSnape.avg_grade(RWeasley, 'Python')
#
# HSlughorn.avg_grade(RWeasley, 'Java')
# HSlughorn.avg_grade(HPotter, 'Java')

HPotter.rate_mntr(MMcConnagal, 'Git', 10)
HPotter.rate_mntr(RLupin, 'MatLab', 8)

RWeasley.rate_mntr(MMcConnagal, 'Git', 8)
RWeasley.rate_mntr(RLupin, 'MatLab', 24)

# HPotter.avrg_rd()
# RWeasley.avrg_rd()

# SSnape.avg_ttl_grds('Python')
# HSlughorn.avg_ttl_grds('Java')

MMcConnagal.avrg_rd()
RLupin.avrg_rd()
# SSnape.comp(HPotter,RWeasley, 'Python')
# HSlughorn.comp(HPotter, RWeasley, "Java")

LecturerList.sort()

# MMcConnagal.com(RLupin)
# print(lecturer.bestlist)

# print(RLupin.bestlist)

print (HPotter)
print (RWeasley)
print(SSnape)
print(HSlughorn)
MMcConnagal.print_best()
# print(RLupin)
StudentList.sort()
# print(LecturerList)
HPotter.print_best()
print(MMcConnagal.avrg_rd)