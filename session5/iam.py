class Person:

    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

class Professor:

    def __init__(self, courses, contract_length=5):
        super().__init__(name, age. courses)
        self.contract_length = contract_length


class Student(Person):

    def __init__(self, name, age, courses, id, grad_year):
        super().__init__(name, age,  courses)
        self.id = id
        self.grad_year = grad_year


class Course:

    def __init__(self, name, professors=None, syllabus=None, policy=None):
        self.name = name
        self.professors = professors
        self.syllabus = syllabus
        self.policy = policy

class Section(Course):
    
    def __init__(self, name, prof, time, students=None, professors=None, syllabus=None, policy=None):
        super().__init__(name, professors, syllabus, policy)
        self.prof = prof
        self.time = time
        self.students = students


    def number_of_students(self):
        return len(self.students)
        

class Class:

    def __init__(self, owner, class_time, section=None):
        self.owner = owner
        if section is None:
            self.section = Section(f"{self.owner}'s class", owner, time)
        else:
            self.section = section
        self.class_time = time

    def start_session(self):
        pass

    def start_poll(self):
        pass

    def end_poll(self):
        pass

    def send_breakout():
        l = self.section.number_of_students()
        # add logic for sending to breakouts
        pass

    def end_session(self):
        pass







