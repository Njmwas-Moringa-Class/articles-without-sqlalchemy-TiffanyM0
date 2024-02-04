class Magazine:
    pass

    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all_magazines.append({name : category})

    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name 
    def getCategory(self):
        return self._category
    def setCategory(self, category):
        self._category = category
    name = property(getName, setName)
    category = property(getCategory, setCategory)

    def name(self):
        return self._name
    
    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls.all_magazines
       
    
bridal = Magazine("Bridal", "wedding")
minis = Magazine("minis", "drinks")
lokko = Magazine("lokko", "fun")

# print(bridal.name())
# print(bridal.category())
# print(bridal.all_magazines)
m1 = Magazine("M1", "life")
m2 = Magazine("M2", "fan")
m3 = Magazine("M3", "man")
m4 = Magazine("M4", "can")
m5 = Magazine("M5", "ran")
m6 = Magazine("M6", "pan")
m7 = Magazine("M7", "son")

# print(Magazine.all())



#def some():
    #pass
    # print(bridal.category)
    # bridal.setCategory("Kenyan Weddings")
    # print(bridal.category)

    # class Student:
    #     def __init__(self, name, age, grade):
    #         self.name = name
    #         self.age = age
    #         self.grade = grade
    #     def get_grade(self):
    #         return self.grade
        
    # class Course:
    #     def __init__(self, name, max_students):
    #         self.name = name
    #         self.max_students = max_students
    #         self.students = [] # works when defining attributes
        
    #     def add_student(self, student):
    #         if len(self.students) < self.max_students:
    #             self.students.append(student)
    #             return True
    #         return False
        
    #     def get_average_grade(self):
    #         pass
    #         value = 0
    #         for student in self.students:
    #             value += student.get_grade()
    #         return value / len(self.students)

    # s1 = Student("Tim", 19, 95)
    # s2 = Student("Bill", 20, 85)
    # s3 = Student("Lala", 35, 98)

    # course = Course("anime-art", 2)
    # course.add_student(s1)
    # course.add_student(s2)

    # print(course.students[0].name)
    # print(course.name)
    # print(course.get_average_grade())

    # #Inheritance
    # class Pet:
    #     #generalization
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age
        
    #     def show(self):
    #         print(f"{self.name}")


    # class Cat(Pet): #inherit properties of pet class
    #     def __init__(self, name, age, color):
    #         super().__init__(name, age) # reference parent class, init, arguments, 
    #         #no need to redifine name, age. 
    #         self.color = color

    #     def speak(self):
    #         print("Meow")
    #     def show(self):
    #         print(f"{self.name}, {self.color}")

    # p = Pet("nana", 3)
    # c = Cat("Lala", 9, "blue" )
    # c.show()

    # p.show()

    # class Dog(Pet):
    #     def speak(self):
    #         print("Bark")

    ## class attributes
    # class Person:
    #     number_of_people = 0
    #     # constant defined as below: 
    #     GRAVITY = -9.8
    #     # does not use self, has no access to instance of a class
    #     # for the whole class, no change from person to person. 
    #     def __init__(self, name):
    #         self.name = name
    #         # Person.number_of_people += 1
    #         Person.add_person()
    #     #class methods: act on the class, no access to instance, cls passed
            
    #     @classmethod
    #     def number_of_pple(cls):
    #         return cls.number_of_people
        
    #     @classmethod
    #     def add_person(cls):
    #         cls.number_of_people += 1

    # p1 = Person("jojo")
    # p2 = Person("kai")
    # print(Person.number_of_pple())# changes for both below.

    # print(p1.number_of_people)
    # print(Person.number_of_people)

    #static methods - called at any point, not dependant on instance, do not change anything
    # class Math:
    #     @staticmethod
    #     def add5(x):
    #         return x + 5
        
    #     @staticmethod
    #     def pr():
    #         return print ("RUN ")

    # Math.pr()