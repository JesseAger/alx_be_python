from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")


def calculate_future_date(days_ahead):
    future_date = (datetime.now() + timedelta(days=days_ahead))
    print(f"Date after {days_ahead} days: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")


display_current_datetime()

days_ahead = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days_ahead)
