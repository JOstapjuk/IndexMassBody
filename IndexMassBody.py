import math
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis on sinu nimi? ")
print(nimi,", oi kui ilus nimi!")
vastus=int(input(nimi+ "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if vastus==1:
    pikkus=float(input("Mis on sinu pikkus? "))
    if pikkus<0:
        tulemus=print("Vale andmed!")
    mass=float(input("Mis on sinu kaal? "))
    if mass<0:
        tulemus=print("Vale andmed!")
    index= mass/math.sqrt(0.01*pikkus)
    print("Sinu keha indeks on: ",round(index,1))
    if index<16:
        vastus="Tervisele ohtlik alakaal"
    elif 16<=index<19:
        vastus="Alakaal"
    elif 19<=index<25:
        vastus="Normaalkaal"
    elif 25<=index<30:
        vastus="Ülekaal"
    elif 30<=index<35:
        vastus="Rasvumine"
    elif 35<=index<40:
        vastus="Tugev rasvumine"
    elif index>40:
        vastus="Tervisele ohtlik rasvumine"
    print(vastus)
else:
    print("Kahju! See on väga kasulik info!")
    print()
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")