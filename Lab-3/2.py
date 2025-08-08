def power(base, exponent=2):
    return base ** exponent

base = float(input("Enter base: "))
exp_choice = input("Enter exponent (leave blank for default 2): ")
if exp_choice.strip() == "":
    print(power(base))
else:
    print(power(base, float(exp_choice)))
