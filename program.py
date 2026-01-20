from modules import show_all_movies
import random
import time


while True:
    print("Menyalternativ")
    print("1. Visa alla filmer")
    print("2. Få ett slumpmässigt filmförslag")
    print("3. Gissa film från beskrivning")
    print("4. Avsluta")
    user_input = input("-> ")

    # Konvertera user input till int - felhantering? try <--> except
    user_input = int(user_input)

    # Menyval
    match user_input:
        case 1:
            show_all_movies()
            print("Tryck på 'Enter' för att återgå till menyn.")
            input()
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Avslutar programmet om 3 sekunder...")
            time.sleep(3) # Pausar programmet i 3sek innan det avslutas
            break
        case _:
            print("Felaktig inmatning. Tryck på 'Enter' för att försöka igen.")
            input()
            continue