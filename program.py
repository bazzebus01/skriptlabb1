from module import show_all_movies

while True:
    print("Menyalternativ")
    print("1. Visa alla filmer")
    print("2. Få ett slumpmässigt filmförslag")
    print("3. Gissa film från beskrivning")
    print("4. Avsluta")
    user_input = input("-> ")
    user_input = int(user_input)

    match user_input:
        case 1:
            show_all_movies()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print("Felaktig inmatning. Var god försök igen. \n\n")
            continue