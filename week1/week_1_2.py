from datetime import date

def get_user_birthday(birth_month: int, birth_date: int):
    """
    Calculates the number of days until the next birthday.
    
    If the birthday is February 29th, in non-leap years it resolves to March 1st.
    """
    today = date.today()
    current_year = today.year

    # Attempt to construct the birthday date for the current year.
    # Handles Feb 29 in non-leap years.
    try:
        next_birthday = date(current_year, birth_month, birth_date)
    except ValueError:
        if birth_month == 2 and birth_date == 29:
            next_birthday = date(current_year, 3, 1)
        else:
            raise ValueError("Invalid birth date or month provided.")

    # If the birthday has already passed this year, target next year.
    if next_birthday < today:
        try:
            next_birthday = date(current_year + 1, birth_month, birth_date)
        except ValueError:
            if birth_month == 2 and birth_date == 29:
                next_birthday = date(current_year + 1, 3, 1)
            else:
                raise ValueError("Invalid birth date or month provided.")

    time_difference = next_birthday - today
    return time_difference.days

if __name__ == "__main__":
    try:
        birthday_input = input("Enter your birthday (DD-MM): ")
        parts = birthday_input.split('-')
        if len(parts) != 2:
            raise ValueError("Date must be in DD-MM format.")
        
        birth_date = int(parts[0])
        birth_month = int(parts[1])
        
        my_days_left = get_user_birthday(birth_month, birth_date)
        if my_days_left == 0:
            print("Happy Birthday!")
        else:
            print(f"Days left until next birthday: {my_days_left}")
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Error: Please enter valid integer numbers.")
        else:
            print(f"Error: {e}")

