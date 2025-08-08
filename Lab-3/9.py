temps_celsius = list(map(float, input("Enter temperatures in Celsius separated by space: ").split()))
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
print("Fahrenheit:", temps_fahrenheit)
