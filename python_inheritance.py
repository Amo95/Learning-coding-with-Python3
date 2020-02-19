# defining superclass
class Person(object):
    # initializing the variables
    # name = ""
    # age = 0

    # defining constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# definition of subclass starts here
class Student(Person):
    # studentId = ""

    def __init__(self, student_name, student_age, student_id):
        # referring to the super class implicitly (in other words, naming the super class implicitly)
        # we have two wways to make reference to super class implicitly

        # Person.__init__(self, student_name, student_age) # explicitly referring
        # super().__init__(student_name, student_age) # implicitly
        super(Student, self).__init__(student_name, student_age) # implicitly
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # return the value of student Id

# end of subvlass definition

#  create an object of the superclass
if __name__ == "__main__":

    # name = input("Enter full name: ")
    # age = int(input("Enter age: "))
    # index = input("Enter index number: ")

    person1 = Person("Amo James", 25)
    # call member method of objects
    person1.show_age()
    person1.show_name()

    # Create an object of the subvlass
    student1 = Student("Ayim Emma", 20, "04/2017/1810D")
    print(student1.get_id())
    student1.show_name()
