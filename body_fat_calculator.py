#body_fat_calculator.py
#Date: 28/September/2020
#by irving-rs

#Description:
#Body Fat Calculator: Estimates body fat, fat mass and lean mass.

#Details:
#Based on the US Navy formula.
#Metric unit system.
#Two models in one (Male and Female).

#Modules:
from math import log10

#Functions:
def bf(): #Computes the body fat porcentage.
    try:
        if gender == "M" or gender == "m" or gender == "Male" or gender == "male": #For men.
            return 495/(1.0324-0.19077*log10(wst-neck)+0.15456*log10(height)) - 450
        elif gender == "F" or gender == "f" or gender == "Female" or gender == "female": #For women.
            return 495/(1.29579-0.35004*log10(wnr+hip-neck)+0.221*log10(height)) - 450
        else:
            return None
    except:
        return "PLEASE PROVIDE VALID INFORMATION !!"

#Variables:
gender = ""

#Presentation of the game:
print("\nBody Fat Calculator:\n")

#Instructions:
print("Instructions:")
print("You will be asked some questions about your weight and other measurements.")
print("Please use a proper weight scale and a soft (flexible) measuring tape.")

#Main body:
while (gender!="M" and gender!="F"):
    #@LEO1612D
    #CODE OPTIMIZATION
    gender = input("\nEnter (M) for Male and (F) for Female: ").upper() #YOU NEED TO WRITE UPPER ONLY ONCE INSTADE OF 4 TIMES
    if gender== "M" or gender== "MALE": #Cheking if M was selected.
        gender = "M"
    elif gender == "F" or gender== "FEMALE": #Cheking if F was selected.
        gender = "F"
    else: #No valid option.
        print("Unknown gender, try again please.")
weight = float(input("Enter you weight in Kg: ")) #Weight
height = float(input("Enter you height in cm: ")) #Height

if gender == "M": #For men.
    wst = float(input("Enter the length of your waist at the navel level in cm: ")) #Waist (at navel)
elif gender == "F": #For women.
    wnr = float(input("Enter the length of your waist at the narrowest in cm: ")) #Waist (at narrowest)
    hip = float(input("Enter the length of your hip at the widest in cm: ")) #Waist (at widest)
    
neck = float(input("Enter the length of your neck at the narrowest in cm: ")) #Neck (at narrowest)


#EXCEPTION HANDLE
try:
    BF = bf()  # Body fat porcentage.
    FM = weight*BF/100 #Fat mass.
    LM = weight-FM #Lean mass.
    print("\nYour estimated body fat percentage is: ", "{:.2f}".format(BF), "%", sep="")
    print("Your estimated fat mass is:", "{:.2f}".format(FM), "Kg", )
    print("Your estimated lean mass is:", "{:.2f}".format(LM), "Kg\n")
except:
    print('\nPLEASE PROVIDE VALID INFORMATION')


### CHANGES UPPER FUNCTION WRITE ONCE
### TRY EXCEPT EXCEPTION
### I HOPE YOU LIKE THIS OPTIMIZED CHANGES