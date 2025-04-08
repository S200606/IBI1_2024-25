def calculator(weight, strength):
    if weight <= 10 or weight >= 100:
        print("please enter the weight in kilograms")
    else:
        if strength == 120 or strength == 250:
            volume = weight * 15 * 5 /strength
            print("the volume of the drug is", volume, "ml")
            return volume
        else:
            print("please enter the strength of the drug correctly")

#example:
calculator(20, 120)  #the volume of the drug is 12.5 ml
calculator(101,120) #please enter the weight in kilograms
calculator(20, 300) #please enter the strength of the drug correctly