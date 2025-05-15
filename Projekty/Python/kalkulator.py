liczba1 = input("Podaj pierwszą liczbe: ")
dzialanie = input("Podaj działanie (+, -, *, /, **, sqrt): ")
if dzialanie == "sqrt":
    wynik = int(liczba1) ** 0.5
else:
    liczba2 = input("Podaj drugą liczbe: ")
    if dzialanie == "+":
        wynik = int(liczba1) + int(liczba2)
    elif dzialanie == "-":
        wynik = int(liczba1) - int(liczba2)
    elif dzialanie == "*":
        wynik = int(liczba1) * int(liczba2)
    elif dzialanie == "/":
        if int(liczba2) == 0:
            print("Nie można dzielić przez zero!")
        else:
            wynik = int(liczba1) / int(liczba2)
    elif dzialanie == "**":
        wynik = int(liczba1) ** int(liczba2)
print(f"Wynik: {wynik}")