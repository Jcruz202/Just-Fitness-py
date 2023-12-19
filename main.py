def main():
    print("Welcome to Just Fitness\n")
    getInfo()
    

def getInfo():
    firstName = input("Please enter your first name: ")
    lastName = input("Enter your last name: ")
    print("\nYour full name is: ", firstName, lastName)

    gender = ("What's your gender(male or female only): ")
    age = int(input("Enter Age (number only): "))
    heightFt = int(input("Enter height (feet): "))
    heightIn = int(input("Enter height (inches): "))
    weight = float(input("Enter weight (lbs): "))

    print("\nYou're ", age, " years of age ", heightFt, "'", heightIn, " tall", sep='')
    print("You weigh", weight, "lbs.")

    bmi = getBMI(heightFt, heightIn, weight)
    formatted_bmi = "{:.3f}".format(bmi)
    print("Your BMI is:", formatted_bmi,"\n")

    if bmi < 18.5:
        print("You're underweight, I can recommend a food diet and workout to gain weight\n")
        yesOrNo = input("Type Y for yes or N for no: ")
    elif bmi >= 18.5 and bmi < 25:
        print("You're healthy!")
        print("Would you like me to recommend you a food diet and a workout plan?")
        yesOrNo = input("Type Y for yes or N for no: ")
        if yesOrNo.lower() == 'y':
            bulkOrCut = input("Bulking or cutting? ")
            if bulkOrCut.lower() == "bulking" or bulkOrCut.lower() == "b":
                foodForBulking()
            elif bulkOrCut.lower() == "cutting" or bulkOrCut.lower() == "c":
                foodForCutting()
            else:
                print("Invalid Input, please type bulking or cutting")
        elif yesOrNo.lower() == 'n':
            print("Thank you for using the app")
        else:
            print("Invalid input")

    elif bmi >= 25 and bmi < 30:
        print("You're overweight, I can recommend a food diet and a workout for cutting\n")
        yesOrNo = input("Type Y for yes or N for no: ")
    elif bmi >= 30:
        print("You're obese")
        print("You're fatass need to lose some weight, here's a food diet and a workout plan to lose weight")

def getBMI(heightFt, heightIn, weight):
    heightTotal = (heightFt * 12) + heightIn
    heightTotalSquared = heightTotal ** 2
    bmi = 703 * weight / heightTotalSquared
    return bmi

def foodForCutting():
    cutFood = ["lean meat", "poultry", "oily fish", "eggs",
               "milk", "yogurt", "low fat cheese", "beans", "nuts" 
                "avocados", "olives", "peas"]
    proteinPowder = ["whey", "hemp"]
    carbs = [ "brown rice", "pasta", "oats", "whole grain bread", "barley", "quinoa"]

    print("\nHere are some recommended food for cutting: ")
    for food in cutFood:
        print(food)
    print("\nHere are some recommended carbs for cutting: ")
    for food in carbs:
        print(food)

def foodForBulking():
    bulkFood = ["Chicken", "Lean Beef", "Eggs", "Rice", "Sweet Potatoes", "Oats",
                "Greek yougurt", "Salmon", "Nuts", "Beans and Legumes"]
    print("\nHere are some recommended food for cutting: ")
    for food in bulkFood:
        print(food)

# def cuttingWorkout():

# def bulkingWorkout():

main()
