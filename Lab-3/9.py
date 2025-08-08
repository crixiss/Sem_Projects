temps_celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
print("Fahrenheit:", temps_fahrenheit)
