import klasser

"""
I filen example.py
gjør vi et "kall" til filen klasser.py via import
slik at vi får tilgang til alle funksjonene og klassene i klasser.py
og kan bruke dem i example.py programmet

"""

# lager nye objekter som arver fra Student klassen
student1 = klasser.Student("John", 25, "B+", "STEM")
student2 = klasser.Student("Jane Doe", 22, "A", "Mathematics")
student3 = klasser.Student("Anonymous", 00, "A", "Computer Security")

student1.get_information()
student2.get_information()
student3.get_information()


# lager nye objekter som arver fra Pythagoras klassen
katet1 = klasser.Pythagoras(12, 25)
katet2 = klasser.Pythagoras(5, 5)

katet1.theorem()
katet2.theorem()

# lager et nytt objekt som arver fra Animal klassen.
dog = klasser.Animal("dog", "woof")
cat = klasser.Animal("cat", "meow")
rabbit = klasser.Animal("rabbit", "very little")

dog.get_sound()
cat.get_sound()
rabbit.get_sound()
