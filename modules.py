import random

filmer = [
    {
        "titel": "The Godfather",
        "genre": "Drama",
        "beskrivning": "Den åldrande patriarken i en organiserad brottsdynasti överför kontrollen över sitt hemliga imperium till sin motvillige son."
    },
    {
        "titel": "The Lord of the Rings",
        "genre": "Fantasy",
        "beskrivning": "Gandalf och Aragorn leder Männens Värld mot Saurons armé för att dra hans blick från Frodo och Sam när de närmar sig Doomberget med Den Ena Ringen."
    },
    {
        "titel": "Pulp Fiction",
        "genre": "Drama",
        "beskrivning": "Livet för två maffiatorrödrar, en boxare, en gangster och hans fru, och ett par dinerbanditer flätas samman i fyra berättelser om våld och försoning."
    },
    {
        "titel": "Forrest Gump",
        "genre": "Drama",
        "beskrivning": "USA:s historia från 1950- till 70-talen utvecklas ur perspektivet av en man från Alabama med ett IQ på 75, som längtar efter att återförenas med sin barndomskärlek."
    },
    {
        "titel": "The Matrix",
        "genre": "Sci-Fi",
        "beskrivning": "När en vacker främling leder datahackern Neo till en hemsk undre värld upptäcker han den chockerande sanningen – livet han känner till är ett utarbetat bedrägeri från en ond cyberunderrättelsetjänst."
    },
    {
        "titel": "Interstellar",
        "genre": "Sci-Fi",
        "beskrivning": "När jorden blir obeboelig i framtiden får bonden och före detta NASA-piloten Joseph Cooper i uppdrag att styra en rymdfarkost, tillsammans med ett team av forskare, för att hitta en ny planet för människor."
    },
    {
        "titel": "Alien",
        "genre": "Sci-Fi",
        "beskrivning": "Efter att ha undersökt en mystisk överföring av okänt ursprung stöter besättningen på ett kommersiellt rymdskepp på en dödlig livsform."
    },
    {
        "titel": "The Odyssey",
        "genre": "Fantasy",
        "beskrivning": "Efter det trojanska kriget står Odysseus inför en farlig resa tillbaka till Ithaka, där han möter varelser som cyklopen Polyfemos, sirenerna och Kirke längs vägen."
    },
    {
        "titel": "Avatar: Fire and Ash",
        "genre": "Fantasy",
        "beskrivning": "Jakes och Neytiris familj brottas med sorg och stöter på en ny, aggressiv Na'vi-stam, Ash-folket, som leds av den eldiga Varang, medan konflikten på Pandora eskalerar och ett nytt moraliskt fokus framträder."
    }
]


# def movies_sorted():
# return filmer["titel"]

def show_all_movies():
    # Sortera alfabetiskt by default?
    for film in filmer:
        print("Titel: " + film["titel"])
        print("Genre: " + film["genre"])
        print("Beskrivning: " + film["beskrivning"] + "\n\n")

def random_movie():
        movie_picker = random.randint(0, len(filmer) - 1)
        print()
        print(filmer[movie_picker]["titel"])
        print()

def guess_movie():
    lives = 3
    movie_picker = random.randint(0, len(filmer) - 1)
    print()
    print(filmer[movie_picker]["beskrivning"])
    print()

    while lives > 0: # Ger användaren 3 chanser att gissa rätt film
        user_guess = input("Gissa på filmen: ".lower())

        if user_guess == filmer[movie_picker]["titel"].lower():
            print("\n################\nDu gissade rätt!\n################\n")
            break
        else:
            lives -= 1
            print(f"Du gissade fel, försök igen. Du har {lives} försök kvar.\n")

    if lives == 0:
        print(f"Du förlorade! Filmen var {filmer[movie_picker]["titel"]}.\n")