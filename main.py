def main():
    print("Welcome to Just Fitness\n")
    firstName = input("Please enter your first name: ")
    lastName = input("Enter your last name: ")
    print("\nYour full name is: ", firstName, lastName)

    gender = ("What's your gender(male or female only): ")
    age = int(input("Enter Age (number only): "))
    heightFt = int(input("Enter height (feet): "))
    heightIn = int(input("Enter height (inches): "))
    weight = float(input("Enter weight (lbs): "))

    print("\nYou're ", age, " years of age ", heightFt, "'", heightIn, " tall", sep=' ')
    print("You weigh", weight, "lbs.")

    heightTotal = (heightFt * 12) + heightIn
    heightTotalSquared = heightTotal ** 2
    bmi = 703 * weight / heightTotalSquared
    formatted_bmi = "{:.3f}".format(bmi)

    print("Your BMI is:", formatted_bmi,"\n")
    if bmi < 18.5:
        print("You're underweight, I can recommend a food diet and workout to gain weight\n")
        yesOrNo = input("Type Y for yes or N for no: ")
    elif bmi >= 18.5 and bmi < 25:
        print("You're healthy")
        print("Would you like me to recommend you a food diet and a workout plan?")
        yesOrNo = input("Type Y for yes or N for no: ")
        if yesOrNo == 'Y':
            bulkOrCut = input("Bulking or cutting?")
    elif bmi >= 25 and bmi < 30:
        print("You're overweight, I can recommend a food diet and a workout for cutting\n")
        yesOrNo = input("Type Y for yes or N for no: ")
    elif bmi >= 30:
        print("You're obese")
        print("You're a fatass lose some weight, here's a food diet and a workout plan to lose weight")
main()
