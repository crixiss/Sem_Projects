temps_celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
above_100 = list(filter(lambda f: f > 100, temps_fahrenheit))

print("Above 100°F:", above_100)
