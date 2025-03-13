# walrus operator - operator morsa

name = "Radek"
if name == "Radek":
    print(f"Twoje imię to {name}")

if name := "Tomek":
    print(f"Twoje imię to {name}")

przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
prompt = "Wybierz swoją przekąskę"

# while True:
#     choice = input(prompt)
#     if choice in przekaski:
#         break
#     print("Nie ma")
while (choice := input(prompt)) not in przekaski:
    if choice == "exit":
        break
    print("Nie ma")
