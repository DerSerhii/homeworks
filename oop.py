import datetime


class Employee:

    def __init__(self, name, salary_day):
        self.name = name
        self.salary_day = salary_day

    def __lt__(self, other):
        salary_day = self.salary_day < other.salary_day
        return f"by salary per day comparison is: {salary_day}"

    def __le__(self, other):
        salary_day = self.salary_day <= other.salary_day
        return f"by salary per day comparison is: {salary_day}"

    def __gt__(self, other):
        salary_day = self.salary_day > other.salary_day
        return f"by salary per day comparison is: {salary_day}"

    def __ge__(self, other):
        salary_day = self.salary_day >= other.salary_day
        return f"by salary per day comparison is: {salary_day}"

    def __eq__(self, other):
        salary_day = self.salary_day == other.salary_day
        return f"by salary per day comparison is: {salary_day}"

    def __ne__(self, other):
        salary_day = self.salary_day != other.salary_day
        return f"by salary per day comparison is: {salary_day}"

    def work(self):
        return '\033[33mI come to the office'

    @staticmethod
    def calculation_business_day():
        """ Calculation of business days including the current day from the beginning of the month """

        current_day = datetime.date.today()
        days, bus_days = current_day.day, 0

        # OPTION #1
        # for day in range(1, days + 1):
        #     if datetime.datetime(current_day.year, current_day.month, day).weekday() < 5:
        #         bus_days += 1

        # OPTION #2
        while days > 0:
            if current_day.weekday() < 5:
                bus_days += 1
            current_day -= datetime.timedelta(days=1)
            days -= 1
        return bus_days

    def check_salary(self, amount_day: int, current_salary: str = None):
        """ Default: defines the salary for the amount of days
            Passing the second argument "cur": defines the salary at the current moment from the beginning of the month
            # Note: argument "cur" - case insensitive
        """
        if current_salary == "cur":
            return self.salary_day * self.calculation_business_day()
        return amount_day * self.salary_day


class Recruiter(Employee):

    def __str__(self):
        return f"{self.__class__.__name__}: \t{self.name}"

    def work(self):
        return '\033[31mI come to the office and start to hiring'


class Programmer(Employee):

    def __init__(self, name, salary_day, tech_stack=None):
        super().__init__(name, salary_day)
        self.tech_stack = tech_stack

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __add__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        name = 'Alfa' + self.name + other.name
        salary_day = self.salary_day + other.salary_day
        tech_stack = ', '.join(sorted(set(self.tech_stack.split(', ') + other.tech_stack.split(', '))))
        return Programmer(name, salary_day, tech_stack)

    def __lt__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        salary_day = self.salary_day < other.salary_day
        tech_stack = len(self.tech_stack.split(", ")) < len(other.tech_stack.split(", "))
        return f"by the salary per day comparison is: {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

    def __le__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        salary_day = self.salary_day <= other.salary_day
        tech_stack = len(self.tech_stack.split(", ")) <= len(other.tech_stack.split(", "))
        return f"by salary per day comparison is: {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

    def __gt__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        salary_day = self.salary_day > other.salary_day
        tech_stack = len(self.tech_stack.split(", ")) > len(other.tech_stack.split(", "))
        return f"by salary per day comparison is: {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

    def __ge__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        salary_day = self.salary_day >= other.salary_day
        tech_stack = len(self.tech_stack.split(", ")) >= len(other.tech_stack.split(", "))
        return f"by salary per day comparison is: {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

    def __eq__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        salary_day = self.salary_day == other.salary_day
        tech_stack = len(self.tech_stack.split(", ")) == len(other.tech_stack.split(", "))
        return f"by salary per day comparison is: {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

    def __ne__(self, other):
        if not isinstance(other, Programmer):
            return NotImplemented
        salary_day = self.salary_day != other.salary_day
        tech_stack = len(self.tech_stack.split(", ")) != len(other.tech_stack.split(", "))
        return f"by salary per day comparison is: {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

    def work(self):
        return '\033[32mI come to the office and start to coding'


emp1 = Employee("Stepan", 5)
rec1 = Recruiter("Ivan", 100)
prog1 = Programmer('Serhii', 200, 'Python, Git&GitHub, Django, Django Rest Framework')
prog2 = Programmer('Boris', 150, 'Python, Git&GitHub, PyQT5, PyGame')
prog3 = prog1 + prog2
all_empl = [emp1, rec1, prog1]
all_prog = [prog1, prog2, prog3]

for em in all_empl:
    print(f'\033[34mI am a {em.__class__.__name__.lower()} {em.name} and {em.work()} \033[34mevery day')
print('\033[38m')

print(rec1, prog1, sep="\n")
print(rec1 < prog1, "\n")

for prmr in all_prog:
    print(f"\033[33mProgrammer {prmr.name} owns such technologies as: {prmr.tech_stack}")

prmr = prog1
print(f"{prmr.name}'s {prmr.__class__.__name__.lower()} salary: {prmr.check_salary(1, 'cur')}$")

print('\033[38m')
print(prog1 != prog3)
print(prog1 != emp1)
