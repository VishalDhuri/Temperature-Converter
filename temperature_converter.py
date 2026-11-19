
# Temperature Conversion Program
# Internship Task - 01

print("===================================")
print("     TEMPERATURE CONVERTER")
print("===================================")

try:
    temperature = float(input("Enter temperature value: "))

    print("\nSelect the original temperature unit:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        if temperature < -273.15:
            print("Invalid temperature! Below absolute zero.")
        else:
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.15

            print("\nConverted Temperatures:")
            print(f"Fahrenheit: {fahrenheit:.2f} °F")
            print(f"Kelvin: {kelvin:.2f} K")

    elif choice == "2":
        if temperature < -459.67:
            print("Invalid temperature! Below absolute zero.")
        else:
            celsius = (temperature - 32) * 5/9
            kelvin = (temperature - 32) * 5/9 + 273.15

            print("\nConverted Temperatures:")
            print(f"Celsius: {celsius:.2f} °C")
            print(f"Kelvin: {kelvin:.2f} K")

    elif choice == "3":
        if temperature < 0:
            print("Invalid temperature! Below absolute zero.")
        else:
            celsius = temperature - 273.15
            fahrenheit = (celsius * 9/5) + 32

            print("\nConverted Temperatures:")
            print(f"Celsius: {celsius:.2f} °C")
            print(f"Fahrenheit: {fahrenheit:.2f} °F")

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

except ValueError:
    print("Invalid input! Please enter a numeric temperature.")

print("\nThank you for using the Temperature Converter!")
