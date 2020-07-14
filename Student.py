from Person import Person
class Student(Person):
    def get_fullname(self):
        return self.fist_name +" "+ self.last_name + "-st"
