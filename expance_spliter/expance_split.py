def calculate_split(total_amount: float, number_of_people: int) ->None:
    if number_of_people <1:
        raise ValueError("Number of people should not be zero")
    
    share_per_person: float = total_amount / number_of_people

    print(f"Total expance: {total_amount}")
    print(f"Number of people: {number_of_people}")
    print(f"Each person should pay: {share_per_person}")

def main() ->None:
    try:
        total_amount: float = float(input("Enter the amount of money: "))
        number_of_people: int = int(input("Enter the number of people: "))

        calculate_split(total_amount,number_of_people)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()