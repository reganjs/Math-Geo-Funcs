# Regan 
# Program - Functions
# February 8th, 2021

# A program written in Python that solves elementary geometry questions
# Calculates the area of a rectangle, square and circle in separate functions
# Calculates the perimeter of a rectangle, square and circle in separate functions
# Has a menu style interactive layout

def squarearea():
    side = float(input(' Side: '))
    print("\n Area: {0}".format(str(side * side)))


def squareperimeter():
    side = float(input(' Side: '))
    print("\n Perimeter: " + str(4 * side))


def rectanglearea():
    length = float(input(" Length: "))
    width = float(input(" Width: "))
    print("\n Area: " + str(length * width))


def rectangleperimeter():
    length = float(input(" Length: "))
    width = float(input(" Width: "))
    print("\n Perimeter: " + str((2 * length) + (2 * width)))


def circlearea():
    radius = float(input(" Radius: "))
    print("\n Area: " + str(3.14 * radius * radius))


def circleperimeter():
    radius = float(input(" Radius: "))
    print("\n Perimeter: " + str(2 * 3.14 * radius))


def menu():
    menuitems = ["AREA (SQUARE)", "AREA (RECTANGLE)", "AREA (CIRCLE)", "PERIMETER (SQUARE)", "PERIMETER (RECTANGLE)",
                 "PERIMETER (CIRCLE)", "EXIT"]

    print("\n\n")

    for i in range(0, 7):
        print("\n " + str(i + 1) + ") " + menuitems[i])

    print("\n\n INPUT MENU CHOICE (1,2,3,4,5,6 OR 7)? ")
    choice = int(input())

    if 1 <= choice <= 7:
        print("\n YOU HAVE CHOSEN " + menuitems[choice - 1])
    else:
        print('\n\n Invalid Option... \n')

    return choice


def main():
    choice = menu()
    while choice != 7:
        if choice == 1:
            squarearea()
        elif choice == 2:
            rectanglearea()
        elif choice == 3:
            circlearea()
        elif choice == 4:
            squareperimeter()
        elif choice == 5:
            rectangleperimeter()
        elif choice == 6:
            circleperimeter()
        else:
            print("\n\n Invalid Option... \n\n")
        choice = menu()


# Calling main function
if __name__ == "__main__":
    main()
