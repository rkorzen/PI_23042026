def calculate_bmi(weight, height):
    return weight / (height * height)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "Waga prawidlowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otylosc"