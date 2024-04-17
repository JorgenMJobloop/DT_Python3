import math
"""
##########
Alle klassene våre

"""


class Animal:
    # konstruktøren
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound
    
    def get_sound(self):
        print(f"A {self.species} says {self.sound}")

class Pythagoras:
    # konstruktøren
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # Klasse funskjon, kan kalles fra andre python programmer i main.py eller andre python filer så lenge det importeres!
    def theorem(self):
        # a^2+b^2=c^2
        a = self.a**2
        b = self.b**2
        c = (a + b)**2
        result = math.sqrt(c)
        print(f"Hypotenusen av den rettvinklede trekentaken med katet A = {a} og katet B = {b} C = {result}\n")

# En veldig "beskrivende" klasse, som har mulighet for å bli veldig stor og holde styr på veldig mye forskjellig data    
class Student:
    # Konstruktøren
    def __init__(self, name, age, grade, subject):
        self.name = name
        self.age = age
        self.grade = grade
        self.subject = subject
    # En funksjon som gir oss nyttig informasjon om studentene.
    def get_information(self):
        print(f"Name: {self.name}\n Age: {self.age}\n current grade: {self.grade}\n and they are studying the following subject: {self.subject}\n")    


"""
#############
Alle objekter som arver fra klassene våre

"""



# # lager nye objekter som arver fra Student klassen
# student1 = Student("John", 25, "B+", "STEM")
# student2 = Student("Jane Doe", 22, "A", "Mathematics")
# student3 = Student("Anonymous", 00, "A", "Computer Security")

# student1.get_information()
# student2.get_information()
# student3.get_information()
# student1.grade
# student2.age
# student3.subject

# # lager nye objekter som arver fra Pythagoras klassen
# katet1 = Pythagoras(12, 25, any)
# katet2 = Pythagoras(5, 5, any)

# katet1.theorem()
# katet2.theorem()

# # lager et nytt objekt som arver fra Animal klassen.
# dog = Animal("dog", "woof")
# cat = Animal("cat", "meow")
# rabbit = Animal("rabbit", "very little")

# dog.get_sound()
# cat.get_sound()
# rabbit.get_sound()


"""
Alle funksjonen våre


"""

def en_funksjon():
    pass