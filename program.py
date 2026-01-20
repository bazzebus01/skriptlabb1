from modules import show_all_movies
from modules import random_movie
from modules import guess_movie
import time


while True:
    print("Menyalternativ")
    print("1. Visa alla filmer")
    print("2. Få ett slumpmässigt filmförslag")
    print("3. Gissa film från beskrivning")
    print("4. Avsluta")
    user_input = input("-> ")

    try: # Kontrollerar att inmatningen är en siffra och konverterar den
        user_input = int(user_input)
    except:
        print("\nFelaktig inmatning, vänligen skriv en siffra.\n")
        continue


    # Menyval
    match user_input:
        case 1:
            show_all_movies()
            print("Tryck på 'Enter' för att återgå till menyn.")
            input()

        case 2:
            random_movie()

        case 3:
            guess_movie()

        case 4:
            print("Avslutar programmet om 3 sekunder...")
            time.sleep(3) # Pausar programmet i 3sek innan det avslutas
            break

        case _:
            print("\nFelaktig inmatning. Vänligen välj en av menyvalen.\n")
            continue