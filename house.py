def main():
    # get name for houses
    name = input("What's your name? ")

    # generate house
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Griffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

main()
