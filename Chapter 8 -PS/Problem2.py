def cel_to_fahrenheit(celcius):
    r=round((celcius*(9/5) + 32),2)
    return r
celcius=int(input("Enter the celcius "))
print(f"The fahrehheit of the celsius is {cel_to_fahrenheit(celcius)}°C")