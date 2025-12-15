class school:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def stude_details(self):
        print(f"Student name:{self.name}")
        print(f"RollNo:{self.rollno}")

class course(school):
    def __init__(self, name, rollno,subject):
        super().__init__(name, rollno)
        self.subject = subject

    def stude_details(self):
        super().stude_details()
        print(f"Subject:{self.subject}")


details = school("sahal",1)
sub = course("shalu",28,"science")
details.stude_details()
sub.stude_details()