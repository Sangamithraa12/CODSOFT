def display_menu():
    print("***************************")
    print("       Simple Calculator   ")
    print("***************************")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("---------------------------")


def get_user_choice():
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def perform_calculation(choice, num1, num2):
    if choice == '1':
        return num1 + num2, "+"
    elif choice == '2':
        return num1 - num2, "-"
    elif choice == '3':
        return num1 * num2, "*"
    elif choice == '4':
        if num2 == 0:
            return None, "/"
        else:
            return num1 / num2, "/"


def main():
    display_menu()

   
    choice = get_user_choice()

    
    print("\nEnter the two numbers for the calculation:")
    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")

    
    result, operator = perform_calculation(choice, num1, num2)

    
    print("\nResult:")
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

    print("\nThank you for using the Simple Calculator!")


if __name__ == "__main__":
    main()
