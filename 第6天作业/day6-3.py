class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(self.name)
        print(self.age)
        print(self.gender)

class Student(Person):
    def __init__(self, name, age, gender, college, class_):
        super().__init__(name, age, gender)
        self.college = college
        self.class_ = class_

    def personInfo(self):
        super().personInfo()
        print(self.college)
        print(self.class_)

    def __str__(self):
        return f'''name: {self.name}\nage: {self.age}\ngender: {self.gender}
college: {self.college}\nclass: {self.class_}'''
    
a = Student("abc",18,"male","xjtu","101")
a.personInfo()
print(a)
