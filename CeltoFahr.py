"""
def cel_to_fahr(cel):
    return (cel * 9/5) + 32

cel = float(input("Enter temperature in Celsius: "))
fahr = cel_to_fahr(cel)
print("Temperature in Fahrenheit:", fahr)


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = "{:.2f}".format((celsius * 9/5) + 32)
print("Temperature in Fahrenheit:", fahrenheit)

"""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = f"{(celsius * 9/5) + 32:.2f}"
print("Temperature in Fahrenheit:", fahrenheit)

