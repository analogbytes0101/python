# Main function
def main():
    # Ask user for their name and format
    inputname = input("What's your name? ").strip().title()

    # Split user name into first and last name
    firstname, lastname = inputname.split(" ")
    
    hello(firstname)

# Hello function
def hello(to="world"):
    # Say hello to user
    print(f"Hello, {to}!")

main()
