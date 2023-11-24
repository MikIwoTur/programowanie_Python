from statistics import mean


class Human:

    # zmienna klasowa - 'globalna'
    Number_of_humans = 0

    def __init__(self, name, age):

        # pola zmiennych instacji klasy
        self.name = name
        self.age = age

        Human.Number_of_humans += 1

    def introduce(self):
        print(f'Hi, nazywam się {self.name} i mam {self.age} lata')


class Student(Human):

    def __init__(self, name, age, program):

        super().__init__(name, age)

        self.program = program
        self.grades = []

    def introduce(self):
        print(
            f'Hi, nazywam się {self.name}, studjuję {self.program} i mam {self.age} lata')

    def __lt__(self, other):
        mean_self = mean(self.grades)
        mean_other = mean(other.grades)
        return mean_self < mean_other

    def recive_grade(self, grade):
        self.grades.append(grade)


osoba1 = Student('Marek', 33, 'Łowiectwo')
osoba2 = Student('Łukasz', 27, 'Wariactwo')
osoba1.recive_grade(4)
osoba1.recive_grade(2)
osoba1.recive_grade(3)
osoba1.recive_grade(4)
osoba2.recive_grade(3)
osoba2.recive_grade(1)
osoba2.recive_grade(3)
osoba2.recive_grade(2)
Studenci = [osoba1, osoba2]
sorted_student = max(Studenci, key=lambda student: mean(student.grades))
highest_mean = mean(sorted_student.grades)
print(f"Oto student z najwyzsza srednia: {sorted_student.name}, {highest_mean}")
