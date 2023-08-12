def main():
    # get number to check
    x = int(input("What's x? "))
    
    #print even or odd
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

def is_even(n):
    # check for parity
    return n % 2 == 0

main()
