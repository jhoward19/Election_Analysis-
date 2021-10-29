counties = ["Arapahoe", "Denver", "Jefferson"]
if counties [1] == 'Denver':
    print(counties[1])

#What is the score? 
score = int(input("What is your test score?"))

#Determine the grade. 
if score  >= 90:
    print('Your grade is an A')
else:
    if score >= 80:
        print('Your grade is a B.')
    else: 
        if score >= 70: 
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else: 
                print('Your grade is a F.')

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
     print('Your grade is an F.')


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)


numbers = [0, 1, 2, 3, 4]
for num in numbers: 
    print(num)

numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)

counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}
for county in counties_dict:
    print(county)

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}
for county in counties_dict.keys(): 
    print(county)

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}
for voters in counties_dict.values():
    print(voters)

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}
for county, voters in counties_dict.items():
    print(county + "county has" + str(voters) + "registered voters")
