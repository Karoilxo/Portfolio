import random
import time

Portfel = 100
graj_dalej = True
while graj_dalej and Portfel > 0:

    liczby = (
            "\033[37;41m 3 \033[0m\033[37;40m 6 \033[0m\033[37;41m 9 \033[0m\033[37;41m12 \033[0m\033[37;40m15 \033[0m"
            "\033[37;41m18 \033[0m\033[37;41m21 \033[0m\033[37;40m24 \033[0m\033[37;41m27 \033[0m\033[37;41m30 \033[0m"
            "\033[37;40m33 \033[0m\033[37;41m36 \033[0m\n"
    
            "\033[37;40m 2 \033[0m\033[37;41m 5 \033[0m\033[37;40m 8 \033[0m\033[37;40m11 \033[0m\033[37;41m14 \033[0m"
            "\033[37;40m17 \033[0m\033[37;40m20 \033[0m\033[37;41m23 \033[0m\033[37;40m26 \033[0m\033[37;40m29 \033[0m"
            "\033[37;41m32 \033[0m\033[37;40m35 \033[0m\n"
    
            "\033[37;41m 1 \033[0m\033[37;40m 4 \033[0m\033[37;41m 7 \033[0m\033[37;40m10 \033[0m\033[37;40m13 \033[0m"
            "\033[37;41m16 \033[0m\033[37;41m19 \033[0m\033[37;40m22 \033[0m\033[37;41m25 \033[0m\033[37;40m28 \033[0m"
            "\033[37;40m31 \033[0m\033[37;41m34 \033[0m\n"
    
            "\033[37;40m" + " " * 6 + "Black" + " " * 7 + "\033[0m"
        "\033[37;41m" + " " * 7 + "Red" + " " * 8 + "\033[0m"
    )
    pola = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, "black", "red"]
    czarne = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    czerwone = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    print(f"♣️ Witaj, oto stół to Ruletki ❤️ \n")
    print(liczby)
    print(f"\n💲 Twój balans wynosi {Portfel}$ \n")
    while True:
        bet_str = input("\n Wybierz pola, ktore chcesz obstawić: ")
        bet_int = bet_str.split()

        valid = True
        valid_bets = []
        for bet in bet_int:
            # Sprawdź liczby
            if bet.isdigit():
                num = int(bet)
                if int(bet) in pola:
                    valid_bets.append(num)
                else:
                    print(f"❌ Nieprawidłowy numer: {bet}")
                    valid = False
                    break
            # Sprawdź kolory
            elif bet.lower() in ['red', 'black']:
                valid_bets.append(bet.lower())
            else:
                print(f"❌ Nieprawidłowy nazwa koloru: {bet}")
                valid = False
                break

        if valid:
            break  # Wszystkie pola OK
        else:
            print("Spróbuj ponownie!")
            """    if bet_str not in pola:
            print("\n ❌ Nie ma takiego pola!")
            bet_str = input(" Wybierz pola, ktore chcesz obstawić: ")"""

    #print(bet_int)
    time.sleep(1)
    stawka = input("Jaka kwotę chcesz przeznaczyć? ")
    if int(stawka) > Portfel:
        print("Nie masz wystarczających środków na koncie !!")
        stawka = input("Jaka kwotę chcesz przeznaczyć? ")
    Portfel = Portfel - int(stawka)
    ilosc_betow = len(bet_int)
    stawka_na_jedno = int(stawka) / ilosc_betow

    time.sleep(2)
    print("Trwa losowanie...")
    time.sleep(2)
    wylosowane = random.randint(1, 36)
    print("Koło ruletki powoli zwalnia")
    time.sleep(2)
    print("Kulka przeskakuje miedzy przedziałami")
    time.sleep(2)
    print("Finalnie kulka zatrzymuje się na polu numer...")
    time.sleep(3)
    print(f"\n Wylosowane pole to {wylosowane}\n")
    time.sleep(2)

    Win = False
    Nagroda = 0
    if 'black' in valid_bets and wylosowane in czarne:
        Nagroda = Nagroda + int(stawka_na_jedno) * 2
        Win = True

    if "red" in valid_bets and wylosowane in czerwone:
        Nagroda = Nagroda + int(stawka_na_jedno) * 2
        Win = False

    if wylosowane in valid_bets:
        Nagroda = Nagroda + stawka_na_jedno * 36
        Win = False

    if Win:
        Portfel = Portfel + Nagroda
        print(f"BRAWO! Wygrałeś {Nagroda}$\n")
        print(f"twój balans wynosi {Portfel}$")

    else:
        print(F"Niestety przegrałeś, twój balans wynosi {Portfel}$")

    if Portfel > 0:
        while True:
            wybor = input("Czy chcesz zagrać ponownie? (Tak/Nie): ").strip().lower()
            if wybor in ['tak', 'nie']:
                graj_dalej = (wybor == 'tak')
                break
            else:
                print("Proszę wpisać 'Tak' lub 'Nie'")

    if not graj_dalej:
        print(f"\nDziękujemy za grę! Kończysz z kwotą {Portfel}$")
        break

if Portfel <= 0:
    print("\n❌ Skończyły Ci się środki na koncie. Koniec gry.")