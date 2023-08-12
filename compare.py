def main():
    # get 2 numbers
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    # compare x and y
    if x == y:
        print(f"{x} is equal to {y}")
    elif x > y:
        print(f"{x} is greater than {y}")
    else:
        print(f"{x} is less than {y}")

    # compare to determine equal
    if x < y or x > y:
        print(f"x is not equal to y")
    else:
        print(f"x is equal to y")
    
    if x != y:
        print(f"x is not equal to y")
    else:
        print(f"x is equal to y")

main()
