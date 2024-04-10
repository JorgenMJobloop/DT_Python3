# tildeler variabelen x verdien 10
x = 10
# tildeler variabelen y verdi 5
y = 5

# printer ut verdien til variabelen x
print("x + y =", x + y)

min_string = "Hei, fra en string!"

# print er en function/keyword
print(min_string)

# da kan vi bruke function/keyword input() til å hente inn tekst til konsollen.
navn = input("Hva heter du? ")
alder = int(input("Hvor gammel er du? "))
si_hei = "Hei"
si_alder = ("Du er " + str(alder) + " år gammel!")

# linje 21 og 22 inneholder de første eksempelene
#print("Hei " + navn)
#print("Du er", alder + 10, "år gammel!")

print(si_hei, navn)
print(si_alder)
# variabel av type list.
spill_kart = ["Skog", "Innsjø", "Fjell", "Havet"]

print("Her er noen forskjellige steder du kan utforske: ")
print(spill_kart)

# selv om vi ikke har sagt at dette skal være float, vil variablene automatisk bli tilegnet som float, når vi har desimaler.
x_float = 1.5
y_float = 1.5

# 3, men siden vi har deklarert dem som float, så får vi 3.0
print(x_float + y_float)
