#parent class
class carcolor:
    def __init__(self,colour):
        self.colour = colour
    
    def show_clr(self):
        print(f"Car Color:{self.colour}")

#parent class
class caryear:
    def __init__(self,year):
        self.year = year

    def show_year(self):
        print(f"Car Year:{self.year}")

#multiple inheritance
#child class
class car(carcolor,caryear):
    def __init__(self,name,colour,year):
        self.name = name
        carcolor.__init__(self,colour)
        caryear.__init__(self,year)

    def car_details(self):
        print(f"Car:{self.name}")
        print(f"Color:{self.colour}")
        print(f"Year:{self.year}")

#input
bmw = car("BMW M3","Red",2025)

#print
bmw.car_details()