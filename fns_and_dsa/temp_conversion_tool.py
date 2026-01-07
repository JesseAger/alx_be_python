FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celcius(fahrenheit_int, unit):
    if unit == 'F':
            temp_in_farenheit=fahrenheit_int*FAHRENHEIT_TO_CELSIUS_FACTOR
            print(f"{fahrenheit}°F is {temp_in_farenheit}°C")

    else:
          print("Invalid inputs")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
fahrenheit = int(input("Enter the temprature to convert: "))
fahrenheit_int=fahrenheit-32
convert_to_celcius(fahrenheit_int, unit)


def convert_to_fahrenheit(celsius, unit):
    if unit == 'C':
            temp_in_celsius=celsius_int*CELSIUS_TO_FAHRENHEIT_FACTOR
            print(f"{celsius}°C is {temp_in_celsius}°F")

    else:
          print("Invalid inputs")

celcius = int(input("Enter the temprature to convert: "))
celsius_int=celcius+32
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
convert_to_fahrenheit(celsius_int, unit)
