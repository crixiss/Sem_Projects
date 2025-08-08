temps_celsius = list(map(float, input("Enter temperatures in Celsius separated by space: ").split()))
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
above_100 = list(filter(lambda f: f > 100, temps_fahrenheit))

print("Above 100°F:", above_100)
