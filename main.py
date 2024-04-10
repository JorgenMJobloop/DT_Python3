import modul_eksempel
# variabel med heltall
# x = 10

# print(x)

# def er en forkortelse for define, dette er python spesifikt. ofte kan vi også se void eller function.

# Funksjon med paramter variabler
"""
a (int) første tall
b (int) andre tall

Returns:
    int: summen av a + b
"""
def my_function(a: int, b: int):
    return a + b


# eksempel på å printe ut funksjonen med argumenter til parameteret.
test_function = my_function(5, 10)
print(test_function)

""" \n står for newline, 
og det splitter opp teksten i konsollen 
til en ny linje
"""

print("########## ny linje\n")

print(modul_eksempel.my_string_function("Navn"))

print(modul_eksempel.no_parameters())

print(modul_eksempel.min_test_funksjon(25, 2))

print("############ ny linje\n")

lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"""
En lengde i programmering, beskriver karakter lengden av en oppbygd tekst streng.
Det vil si: for eksempel antall bokstaver i en gitt tekst, hvor det er blitt behandlet
som et array/liste.

"""

print(len(lorem))

"""
For loopen nedenfor "looper" gjennom teksten for hver bokstav, altså 
446 ganger.
Det kan vi gjøre også med en for range loop, med tall.

"""
for tekst in lorem:
    if len(lorem) < 50: 
        print(tekst)
    else:
        print("ingenting skjedde\n")
        break

for ny_tekst in lorem.splitlines():
    print(ny_tekst.replace(",", "AA"))


# for i in range(0, 447):
#     print(i)
