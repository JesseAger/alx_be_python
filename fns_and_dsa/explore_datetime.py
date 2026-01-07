from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%B %d, %Y, %I:%M %p")
    print(f"Current date and time: {current_date}")


def calculate_future_date(days_ahead):
    future_date = datetime.now() + timedelta(days=days_ahead)
    future_date = future_date.strftime("%B %d, %Y")
    print(f"Date after {days_ahead} days: {future_date}")

days_ahead = int(input("Enter number of days to add: "))
calculate_future_date(days_ahead)

