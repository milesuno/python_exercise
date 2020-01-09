# Weight Converter - Working with conditional statements

weight = input("How much do you weigh? ")
kg_or_lb = input("Is that (K)g or (L)b's? ")


def weight_converter(body_weight, weight_unit):
    if weight_unit == "K" or weight_unit == "k":
        print(f"Your weight in Lbs: {int(body_weight) * 2.205}Lbs")
    elif weight_unit == "L" or weight_unit == "l":
        print(f"Your weight in Kgs: {int(body_weight) / 2.205}Kgs")
    else:
        print(f'"{weight_unit}" is not a valid unit measurement. Please choose "K" for Kgs or "L" for Lbs.')


weight_converter(weight, kg_or_lb)
