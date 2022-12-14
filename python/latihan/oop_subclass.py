class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember: {})".format(self.name))
    
    def tell(self):
        '''Tell my details.'''
        print('name:"{}"age:"{}"'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("(Initialized Teacher: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a stuend.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("(Initialized Student: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks: "{}"'.format(self.marks))
t = Teacher('Mrs. Shelly', 25, 3000000)
s = Student('David', 21, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # works for both Teachers and Students
    member.tell()