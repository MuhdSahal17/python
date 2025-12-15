#parent class
class person:
    def __init__(self,name):
        self.name = name

    def show_details(self):
        print(f"Name :{self.name}")

#child class
class student(person):
    def __init__(self, name, RollNo):
        super().__init__(name)
        self.RollNo = RollNo

    def show_details(self):
        super().show_details()
        print(f"RollNo :{self.RollNo}")

#child class
class CollegeStudent(student):
    def __init__(self, name, RollNo, CollegeName):
        super().__init__(name,RollNo)
        self.CollegeName = CollegeName

    def show_details(self):
        super().show_details()
        print(f"College :{self.CollegeName}")

p1 = CollegeStudent("Sahal",1,"GPTC")
p2 = CollegeStudent("Loki",28,"CJHSS")
p3 = CollegeStudent("Hamilton",44,"KSAEMS")

p1.show_details()
p2.show_details()
p3.show_details()