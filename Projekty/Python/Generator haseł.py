import random
print("Generator haseł")
znaki = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ1234567890!@#$%^&*"
haslo = ""
dlugosc_hasla = input("\nPodaj ilość znaków: ")

for x in range(int(dlugosc_hasla)):
    haslo = haslo + random.choice(znaki)

print(f"Wygenerowane hasło: {haslo}")