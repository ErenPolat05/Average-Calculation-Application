

grade1 = int(input("Your 1st Grade: "))
grade2 = int(input("Your 2nd Grade: "))
quiz= int(input("Your Quiz Note: "))

average = (grade1 + grade2 + quiz) /3


if average <= 24:
    print(f"Hello {average} Your Grade: 0")
elif (average >=25) and (average <=44):
    print(f"Hello {average} Your Grade: 1")
elif (average >=45) and (average <=54):
    print(f"Hello {average} Your Grade: 2")
elif (average >=55) and (average <=69):
    print(f"Hello {average} Your Grade: 3")
elif (average >=70) and (average <=84):
    print(f"Hello {average} Your Grade: 4")
elif (average >=85) and (average <100):
    print(f"Hello {average} Your Grade: 5")
else :
    print("Incorrect Grade Entry. Please Try Again.")
